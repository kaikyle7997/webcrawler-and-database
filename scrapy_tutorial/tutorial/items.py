# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass


class FufaItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    pass



class BNCItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    host = scrapy.Field()
    pickup = scrapy.Field()
    dropoff = scrapy.Field()
    price = scrapy.Field()
    details = scrapy.Field()
    pass

class BNCDItem(scrapy.Item):
    host_d = scrapy.Field()
    notes = scrapy.Field()
    feedinto_data = scrapy.Field()
    pass