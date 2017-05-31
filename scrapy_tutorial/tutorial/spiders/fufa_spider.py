import scrapy
from tutorial.items import FufaItem


class FufaSpider(scrapy.Spider):
    name = "fufa"
    allowed_domains = ["fufashoes.com"]
    start_urls = [
        "http://fufashoes.com/GoodList.aspx?s1=1"
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         title = sel.xpath('a/text()').extract()
    #         link = sel.xpath('a/@href').extract()
    #         desc = sel.xpath('text()').extract()
    #         print title, link, desc

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = FufaItem()
            item['title'] = sel.xpath('a/div[3]/text()').extract()
            item['price'] = sel.xpath('a/div[4]/div/span/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item