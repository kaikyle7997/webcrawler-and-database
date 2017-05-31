# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from stackoverflow.items import StackoverflowItem


class SoCrawlingSpider(CrawlSpider):
    name = 'so_crawling'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?sort=featured']

    rules = (
        Rule(LinkExtractor(allow=r'questions\/[0-9]+\/.*'), callback='parse_question', follow=False),
    )

    def parse_start_url(self, response):
        pass

    def parse_question(self, response):
        item = StackoverflowItem()
        item['header'] = response.xpath('//div[@id="question-header"]//a/text()').extract()
        item['solvers'] = response.xpath('//div[@id="answers"]//div[@class="user-details"]/a/text()').extract()
        return item
