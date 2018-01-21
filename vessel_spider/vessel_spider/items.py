# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VesselSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imo = scrapy.Field()
    name = scrapy.Field()
    mmsi = scrapy.Field()
    vessel_type = scrapy.Field()
    gross_tonnage = scrapy.Field()
    summer_dwt = scrapy.Field()
    build_year = scrapy.Field()
    flag = scrapy.Field()
    home_port = scrapy.Field()
