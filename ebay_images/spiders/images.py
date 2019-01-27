# -*- coding: utf-8 -*-
import scrapy
#import re
#import rson
from ebay_images.items import EbayImagesItem

class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["ebay.com","ebayimg.com"]
    start_urls = (
        'https://www.ebay.com/sch/i.html?_from=R40&_nkw=polo+sport&_sacat=0&rt=nc&LH_BIN=1',
    )
    
    def __init__(self, url=None, *a, **kw):
        super(ImagesSpider, self).__init__(*a, **kw)
        if url:
            self.start_urls = (url,)
    
    def parse(self, response):
        response.url == 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=polo&_sacat=0&LH_BIN=1&_sop=10'
        
        #yield the desired page
        yield scrapy.Request(response.url, self.parse_page)
        
    def parse_page(self, response):
        for listing in response.css(".s-item__link").xpath("@href").extract():
            yield scrapy.Request(listing, self.parse_listing)
            
        next_page = response.css(".x-pagination__control").xpath("@href").extract()[1]
        
        if int(next_page[-1]) <= 100:
            print("/n")
            print("/n")
            print("/n")
            print(int(next_page[-1]))
            print("/n")
            print("/n")
            print("/n")
            yield scrapy.Request(next_page, self.parse_page)
        
        
        
    def parse_listing(self, response):    
            
        item = EbayImagesItem()
            
        item['listing_title'] = response.css(".it-ttl::text").extract_first()
            
        item['listing_url'] = response          
            
        item['image_urls'] = [response.css(".img300").xpath("@src").extract()[1]]
            
        item['listing_price'] = response.css(".notranslate::text").extract_first()
            
        #item['shipping_cost'] = response.css(".s-item__shipping::text").extract_first()
            
        yield item
        
            
            
      
  
  
  
  
  
  
  
  
  