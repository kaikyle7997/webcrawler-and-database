import scrapy


class MyItem(scrapy.Item):
    title = scrapy.Field()
    myip = scrapy.Field()


class RandomIPUserAgentSpider(scrapy.Spider):
    name = "rand"

    allowed_domains = [
        'torproject.org',
        'whatismyipaddress.com',
        'iplocation.net',
        'google.com',
    ]

    custom_settings = {
        "DOWNLOAD_DELAY": 5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }

    start_urls = (
        # 'https://check.torproject.org/',
        # 'https://check.torproject.org/',
        # 'https://check.torproject.org/',
        # 'https://check.torproject.org/',
        # 'https://check.torproject.org/',
        'http://whatismyipaddress.com/',
        'http://whatismyipaddress.com/',
        'http://whatismyipaddress.com/',
        'http://whatismyipaddress.com/',
        # 'https://www.iplocation.net/find-ip-address',
        # 'https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=what+is+my+ip',
    )

    def parse(self, response):
        item = MyItem()

        # Get the page title
        item['title'] = response.xpath('//html/head/title/text()').extract()

        # Get IP address, http://whatismyipaddress.com/
        item['myip'] = response.xpath('//*[@id="section_left"]/div[2]/a/text()').extract()

        # Get IP address, https://www.iplocation.net/find-ip-address
        # item['myip'] = response.xpath('//*[@id="wrapper"]/section/div/div/div[1]/div[4]/div[2]/p[1]/span/text()').extract()

        # Get IP address, https://check.torproject.org/
        # item['myip'] = response.xpath('/html/body/div[2]/p[1]/strong/text()').extract()

        yield item
