# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import signals
from lofter.misc.log import *
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class LofterPipeline(object):

    def process_item(self, item, spider):

        if os.path.exists("author"):
            pass
        else:
            os.mkdir("author")
        self.result = codecs.open("./author/"+item['name']+".jpg", 'w')
        #info("item to db:"+ item['title'])
        self.result.write(item['content'])
        self.result.flush()
        return item
