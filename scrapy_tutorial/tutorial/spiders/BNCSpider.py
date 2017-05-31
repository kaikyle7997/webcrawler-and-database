import scrapy
from tutorial.items import BNCItem, BNCDItem


class BNCSpider(scrapy.Spider):
    name = "bnc"
    allowed_domains = ["bluenet-ride.com"]
    start_urls = (
        'https://www.bluenet-ride.com/search-rides',
    )

    def parse(self, response):
        domain = 'https://www.bluenet-ride.com'
        for sel in response.xpath('//*[@id="rideList"]/div[re:test(@class, "rideBox")]'):
            item = BNCItem()
            item['host'] = sel.xpath('a/button[2]/div[1]/h3/text()').extract()
            # item['pickup'] = sel.xpath('div[1]/a/div/div[1]/h3[1]/text()').extract()
            item['pickup'] = sel.xpath('a/div/div[1]/h3[1]/text()[2]').extract()
            item['dropoff'] = sel.xpath('a/div/div[1]/h3[2][1]').extract()
            item['price'] = sel.xpath('a/div/div[3]/div[3]/span/text()').extract()
            item['details'] = domain + sel.xpath('a/@href').extract()[0]
            # //*[@id="rideList"]/div[49]/a/div/div[1]/h3[2]/text()
            # yield item
            # yield scrapy.Request(item['details'], self.parse_detail)
            yield scrapy.Request(item['details'], self.parse_detail, meta={'feedinto': item})

    def parse_detail(self, res):
        item = BNCDItem()
        # item['notes'] = res.xpath('/html/body/div[7]/section[2]/div[1]/p[1]/text()').extract()[0]
        item['host_d'] = res.xpath('/html/body/div[7]/section[3]/div[2]/a/span/text()').extract()[0]
        item['feedinto_data'] = res.meta['feedinto']['price']
        # print(item['notes'])
        yield item
        # return item

        # /html/body/div[7]/section[1]/button/h2[1]

    def parse_response(self, response):
        """
                @url https://www.bluenet-ride.com
                @returns items 1 1
                """
        return BNCItem()