# -*- coding: utf-8 -*-
from scrapy.spiders import Spider, Rule
from scrapy import Request
from stackoverflow.items import StackoverflowItem


class SoRequestSpider(Spider):
    name = 'so_request'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?sort=featured']

    def parse(self, response):
        domain = 'http://stackoverflow.com'
        qss = response.xpath('//div[@class="question-summary"]')
        for qs in qss:
            yield Request(domain + qs.xpath('div[@class="summary"]/h3/a/@href').extract()[0], callback=self.parse_question)

    def parse_question(self, response):
        item = StackoverflowItem()
        item['header'] = response.xpath('//div[@id="question-header"]//a/text()').extract()
        item['solvers'] = response.xpath('//div[@id="answers"]//div[@class="user-details"]/a/text()').extract()
        return item
