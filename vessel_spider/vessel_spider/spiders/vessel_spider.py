import scrapy

class VesselSpider(scrapy.Spider):
    name = "vessel"
    allowed_domains = ["marinetraffic.com"]
    start_urls = [
        "https://www.marinetraffic.com/en/ais/index/search/all?keyword=9632143" # TODO: implement start_url generator
    ]

    def parse(self, response):
        # proceed to further pages
        for page_url in response.css("a[class = search_index_link]::attr(href)").extract():
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)

        # extract vessel information TODO: parse data into proper JSON
        for li in response.css("div[id = vessel_details_general]"):
            yield {
                "row": li.css("span").extract()
            }