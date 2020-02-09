# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
     'https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A360832011&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=d51650ff-60b4-4a83-9258-120554589089&pf_rd_r=RCN03C7QY5F177JEM3NH&pf_rd_s=merchandised-search-4&pf_rd_t=101&ref=s9_acss_bw_cts_AELugg_T2_w'
     ]

    def parse(self, response):
    	items = AmazonItem()
    	#page_limit =response.css('li.a-disabled::text').extract()
    	

    	#product_price = response.css('.a-price-whole::text')
    	#product_description = response.css('.a-color-base.a-text-normal::text')

    	product_price = response.css('.a-price-whole::text')
    	product_description = response.css('.a-color-base.a-text-normal::text')

    	a = len(product_price)
    	b = len(product_description)
    	a = min(a,b)

    	for i in range(a):
    		yield{
    		'product_description':''.join(product_description[i].extract()),
    		'product_price':''.join(product_price[i].extract())
    		}

    	next_page = "https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A360832011&page="+str(AmazonSpiderSpider.page_number)+"&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=d51650ff-60b4-4a83-9258-120554589089&pf_rd_r=RCN03C7QY5F177JEM3NH&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1568831768&ref=sr_pg_2"


    	if AmazonSpiderSpider.page_number<=400:
    		AmazonSpiderSpider.page_number+=1
    		yield response.follow(next_page,callback = self.parse)