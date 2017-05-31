import scrapy
import datetime

class MyItem(scrapy.Item):
    datetime = scrapy.Field()
    ua_req = scrapy.Field()
    ua_echo = scrapy.Field()


class GetUserAgentSpider(scrapy.Spider):
    name = "getua"

    allowed_domains = [
        'whatsmyuseragent.com',
    ]

    start_urls = (
        'http://whatsmyuseragent.com/',
        'http://whatsmyuseragent.com/',
        'http://whatsmyuseragent.com/',
        'http://whatsmyuseragent.com/',
    )

    # user_agent = "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" # Bingbot 2.0

    def parse(self, response):
        item = MyItem()

        item['datetime'] = str(datetime.datetime.now())

        if 'User-Agent' in response.request.headers:
            item['ua_req'] = response.request.headers['User-Agent']

        if response.xpath('//div[@class="col-sm-12 well"]/h2[@class="info"]/text()'):
            item['ua_echo'] = response.xpath('//div[@class="col-sm-12 well"]/h2[@class="info"]/text()').extract()[0]

        yield item
