# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbayImagesItem(scrapy.Item):
    listing_title = scrapy.Field()
    listing_url = scrapy.Field()
    image_urls = scrapy.Field()
    listing_price = scrapy.Field()
    images = scrapy.Field()
    #shipping_cost = scrapy.Field()
    
    
    # might need to change item names 
    # source: https://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/
    #file_urls = scrapy.Field()
    #files = scrapy.Field()