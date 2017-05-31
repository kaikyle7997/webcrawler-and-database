# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open("out.json", "wb", encoding="utf-8")
        # self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        try:
            if item['user'][0] == 'mrzool':  #in self.ids_seen:
                # raise HackerNewsItem("Duplicate item found: %s" % item)
                print('woowwowowowoowAAAAAAAAAAAAAAAAAAAAAAAa')
            else:
                self.ids_seen.add(item['user'])
                return item
        except KeyError:
            # self.ids_seen.add(item['user'])
            return item
