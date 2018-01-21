import scrapy
import csv

class VesselSpider(scrapy.Spider):
    name = "vessel"
    allowed_domains = ["marinetraffic.com"]
    start_urls = []

    # generate start_urls from csv file or use defaults
    def __init__(self, filename):
        if filename:
            with open(filename, newline="") as f:
                reader = csv.DictReader(f)
                base_url = "https://www.marinetraffic.com/en/ais/index/search/all?keyword="
                self.start_urls = [base_url + str(row["Vessel_name"]) for row in reader]
        else:
            self.start_urls = [
                "https://www.marinetraffic.com/en/ais/index/search/imo?keyword=9632143",
                "https://www.marinetraffic.com/en/ais/index/search/all?keyword=101260"
            ]

    def parse(self, response):

        # access search result page
        for result_page in response.css("a[class = search_index_link]::attr(href)"):
            yield response.follow(result_page, callback=self.parse)

        # parse general information TODO: implement xpath logic to deal with variations in  DOM
        raw_keys = response.xpath("//*[@id='vessel_details_general']/div/ul/li/span/text()").extract()
        raw_values = response.xpath("//*[@id='vessel_details_general']/div/ul/li/span/b/text()").extract()

        # clean parsed data TODO: move cleaning logic to item pipeline
        clean_keys = [e.replace(":", "").strip().lower() for e in raw_keys]
        clean_values = [e.replace(" ", "_").lower() for e in raw_values]

        # generate output
        yield {
            k:v for k, v in zip(clean_keys, clean_values)
        }