# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import re
import json
import codecs
from scrapy.conf import settings
from scrapy import log
import pymongo


class StackoverflowPipeline(object):
    def process_item(self, item, spider):
        return item


class ViewPipeline(object):
    def process_item(self, item, spider):
        view_s = item['view']
        view_num = re.compile('([0-9]+)').search(view_s).group(1)
        if int(view_num) > 10:
            item['view'] = view_num
            return item
        else:
            raise DropItem('Item view is too less')


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open("items_pl.json", "wb", encoding="utf-8")
 
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
 
    def spider_closed(self, spider):
        self.file.close()


class MongoPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGO_SERVER'], settings['MONGO_PORT'])
        db = connection[settings['MONGO_DB']]
        self.collection = db[settings['MONGO_COLLECTION']]
 
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        log.msg("Save to MongoDB", level=log.DEBUG, spider=spider)
        return item


