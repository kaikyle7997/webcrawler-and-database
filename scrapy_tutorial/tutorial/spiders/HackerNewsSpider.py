import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging

class HackerNewsItem(scrapy.Item):
    user = scrapy.Field()
    created = scrapy.Field()


class HackerNewsItem2(scrapy.Item):
    first_submission = scrapy.Field()
    submission_age = scrapy.Field()


class HackerNewsItem3(scrapy.Item):
    title = scrapy.Field()


class HackerNewsSpider(CrawlSpider):
    name = 'hackernews'

    # An optional list of strings containing domains that this spider is allowed to crawl.
    # Requests for URLs not belonging to the domain names specified in this list won't be followed
    # if OffsiteMiddleware is enabled.
    # http://doc.scrapy.org/en/latest/topics/spiders.html
    # http://doc.scrapy.org/en/latest/faq.html#i-get-filtered-offsite-request-messages-how-can-i-fix-them
    allowed_domains = ['news.ycombinator.com',
                       'github.io']
    start_urls = [
        'https://news.ycombinator.com/'
    ]

    rules = (
        # Follow any absolute/relative urls that match with regex and call the specified parse_xxxx functions
        # parameter - allow - can be a regex or list of regex
        # http://doc.scrapy.org/en/latest/topics/link-extractors.html
        Rule(LinkExtractor(allow=('user\?.*', )), callback='parse_item', follow=True),

        # If the above follow=False, then this rule has be no action as it will not follow the links of
        # href='submitted\?.*'  in page 'user\?.*'; so can try to change into True or False
        Rule(LinkExtractor(allow=('submitted\?.*', )), callback='parse_beyond', follow=False),

        Rule(LinkExtractor(allow=('.*github\.io.*', )), callback='parse_github', follow=False),
    )

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }

    def parse_item(self, response):
        item = HackerNewsItem()

        # Get the username
        item['user'] = response.xpath('//*[@id="hnmain"]/tr[3]/td/table/tr[1]/td[2]/a/text()').extract()
        # logging.debug(item['user'])

        # Get the created day
        item['created'] = response.xpath('//*[@id="hnmain"]/tr[3]/td/table/tr[2]/td[2]/text()').extract()
        # logging.debug(item['created'])

        return item

    def parse_beyond(self, response):
        item = HackerNewsItem2()
        item['first_submission'] = response.xpath('//*[@id="hnmain"]/tr[3]/td/table/tr[1]/td[3]/a/text()').extract()
        item['submission_age'] = response.xpath('//*[@id="hnmain"]/tr[3]/td/table/tr[2]/td[2]/span[2]/a/text()').extract()
        return item

    def parse_github(self, response):
        item = HackerNewsItem3()
        item['title'] = response.xpath('//title/text()').extract()
        return item
