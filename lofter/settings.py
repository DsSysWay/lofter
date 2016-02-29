# Scrapy settings for lofter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'lofter'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['lofter.spiders']
NEWSPIDER_MODULE = 'lofter.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = {
    'lofter.pipelines.LofterPipeline': 300,        
}

LOG_LEVEL = 'DEBUG'
