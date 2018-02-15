import os
import fnmatch
import csv
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PortSpider(CrawlSpider):
    name = "port"
    allowed_domains = ["marinetraffic.com"]

    # generate start_urls from csv file
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.csv"):
            with open(file, newline="") as f:
                reader = csv.reader(f)
                # skip header
                next(reader, None)
                # build start_urls from clean first column of csv file
                start_urls = ["https://www.marinetraffic.com/en/ais/index/search/all?keyword=" +
                              str(row[0]).strip().lower() for row in reader]

    # define rule to follow links in search result pages
    rules = (
        Rule(LinkExtractor(allow=("https://www.marinetraffic.com/en/ais/details/ports/*", ),
                           restrict_css=("a[class = search_index_link]")), callback="parse_item"),
    )

    def parse_item(self, response):
        """
        Given an url, parse general content tab and return its values as Python dict

        @url https://www.marinetraffic.com/en/ais/index/search/all?keyword=9632143
        @returns items 1
        @returns requests 0 0
        @scrapes
        """

        # parse general information
        info_general = response.xpath("//div[starts-with(@class, 'bg-info')]")
        info_vessels = response.xpath("//table[@id='currvess']")
        info_arrivals = response.xpath("//table[@id='recarr']")
        info_expected = response.xpath("//table[@id='exparr']")
        # use div id since wind forecast table does not have its own id
        info_wind_forecast = response.xpath("//div[@id='tabs-wind-fore']//table")


        # extract specific information
        raw_keys_general = info.general.xpath(".//span/text()").extract()
        raw_values_general = info.general.xpath("//b/text()").extract()
        raw_values_general2 = info_general.xpath("//b/a/text()").extract()

        raw_keys_vessels = info_vessels.xpath(".//a/text()").extract()
        raw_values_vessels = info_vessels.xpath("//a/@href").extract()

        # parse keys
        # raw_keys = list()
        # for span in info_general.xpath(".//span/text()"):
        #     raw_keys.append(span.extract())
        #
        # # parse values
        # raw_values = list()
        # for span in info_general.xpath(".//span/b/text()"):
        #     raw_values.append(span.extract())
        #
        # # clean parsed data TODO: move cleaning logic to item pipeline
        # clean_keys = [e.replace(":", "").replace(" ", "_", 1).strip().lower() for e in raw_keys]
        # clean_values = [e.replace(" ", "_", 1).strip().lower() for e in raw_values]
        #
        # # generate output TODO: use scrapy items instead of python dicts
        # yield {
        #     k:v for k, v in zip(clean_keys, clean_values)
        # }