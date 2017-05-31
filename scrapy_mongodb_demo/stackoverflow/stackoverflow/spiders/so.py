# -*- coding: utf-8 -*-
#import scrapy
#
#
#class SoSpider(scrapy.Spider):
#    name = "so"
#    allowed_domains = ["stackoverflow.com"]
#    start_urls = (
#        'http://www.stackoverflow.com/',
#    )
#
#    def parse(self, response):
#        pass

import scrapy
from stackoverflow.items import StackoverflowItem
 
class SoSpider(scrapy.Spider):
    name = "so"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
        "http://stackoverflow.com/questions?pagesize=50&sort=featured"
    ]
 
    # def parse(self, response):
    #     qss = response.xpath('//div[@class="question-summary"]')
    #     for qs in qss:
    #         item = StackoverflowItem()
    #         item['title'] = qs.xpath('//div[@class="summary"]/h3/a/text()').extract()[0]
    #         item['link'] = qs.xpath('//div[@class="summary"]/h3/a/@href').extract()[0]
    #         item['view'] = qs.xpath('//div[@class="statscontainer"]/div[@class="views "]/text()').extract()[0]
    #         yield item

    def parse(self, response):
        qss = response.xpath('//div[@class="question-summary"]')
        for qs in qss:
            item = StackoverflowItem()
            item['title'] = qs.xpath('div[@class="summary"]/h3/a/text()').extract()[0]
            item['link'] = qs.xpath('div[@class="summary"]/h3/a/@href').extract()[0]
            item['view'] = qs.xpath('div[@class="statscontainer"]/div[@class="views "]/text()').extract()[0]
            yield item