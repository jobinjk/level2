# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Level2Item(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
