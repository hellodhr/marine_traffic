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
        # TODO: double-check if parser tries to parse search result page instead of actual content page
        for result_page in response.css("a[class = search_index_link]::attr(href)"):
            yield response.follow(result_page, callback=self.parse)

        # parse general information
        info_general = response.xpath("//div[@id='vessel_details_general']")

        # parse keys
        raw_keys = list()
        for span in info_general.xpath(".//span/text()"):
            raw_keys.append(span.extract())

        # parse values
        raw_values = list()
        for span in info_general.xpath(".//span/b/text()"):
            raw_values.append(span.extract())

        # clean parsed data TODO: move cleaning logic to item pipeline
        clean_keys = [e.replace(":", "").strip().lower() for e in raw_keys]
        clean_values = [e.replace(" ", "_").lower() for e in raw_values]

        # generate output if parsing is successful
        if len(info_general) > 0:

            yield {
                k:v for k, v in zip(clean_keys, clean_values)
            }