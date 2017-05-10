# -*- coding: utf-8 -*-
import scrapy
from level2.items import Level2Item

class Level2ProductSpider(scrapy.Spider):
    name = "MyntraDeals"
    allowed_domains = ["myntra.com"]
  
  #Use working product URL below
    start_urls = [
         "https://www.myntra.com/tshirts/ether/ether-navy--white-striped-polo-t-shirt/1377369/buy",
        
     ]
 
    def parse(self, response):
        items = Level2Item()
        title = response.xpath('//*[@id="mountRoot"]/div/div/main/div[2]/div[2]/div[1]/h1/text()').extract()
        sale_price = response.xpath('//*[@id="mountRoot"]/div/div/main/div[2]/div[2]/div[1]/p/strong/text()').extract()
        
        items['product_name'] = ''.join(title).strip()
        items['product_price'] = ''.join(sale_price).strip()
        
        yield items

