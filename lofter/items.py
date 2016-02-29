# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class LofterItem(Item):
    # define the fields for your item here like:
     author = Field()
    #pic url
     url = Field()
    # pic name
     name = Field()
    #pic content
     content = Field()
