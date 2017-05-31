import scrapy
import datetime

class MyItem(scrapy.Item):
    myip = scrapy.Field()
    datetime = scrapy.Field()


class GetIpSpider(scrapy.Spider):
    name = "getip"

    allowed_domains = [
        'torproject.org',
        'echoip.com',
    ]

    start_urls = (
        'https://check.torproject.org/',
        'https://check.torproject.org/',
        'https://check.torproject.org/',
        'https://check.torproject.org/',
        # 'http://echoip.com',
        # 'http://echoip.com',
        # 'http://echoip.com',
        # 'http://echoip.com',
    )


    def parse(self, response):
        item = MyItem()

        item['datetime'] = str(datetime.datetime.now())

        # Get IP address from https://check.torproject.org/
        item['myip'] = response.xpath('/html/body/div[2]/p[1]/strong/text()').extract()

        # Get IP address from http://echoip.com
        # item['myip'] = response.body

        yield item
