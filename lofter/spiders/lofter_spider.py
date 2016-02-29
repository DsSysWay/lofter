#coding="utf-8"
import  re
import json
import scrapy

from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from lofter.items import *
from lofter.misc.log import *
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


###URL2_ARTICLE_TITLE = {}

class LofterSpider(CrawlSpider):



    name = "lofter" #here is the key to name spider,if not match will throw spider not found error
    allowed_domains = ["baidu.com"]
    start_urls = [
            "http://www.baidu.com/",
    ]
    rules = [
    #    Rule(sle(allow=("/followees")), follow=True, callback='parse_follow'),
    ]

    headers = { 
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
            "Connection":"keep-alive",
            "Cookie":"firstentry=%2Fblogindex.do%3FloftBlogName%3Djustinbieber520%26X-From-ISP%3D1|; usertrack=c+xxClbQXHstRwvoBiciAg==; _ntes_nnid=89b7fb7e37143430fd28d67dd6195c13,1456495740330; _gat=1; JSESSIONID-WLF-XXD=a5ae0beed9053b5b41a62312cb48f05aefab56c30a2994037be2dc9765904ea36c9ad52b0dfb2060014f412dc05eaf7a1ad33bfb45c0fff5e46f65899601658a1f1faf66775f4813cde895a884fdb375c692b0098a148e7acf0778144fa00331dd712ca588e8a43bbd64b34fae5a943aa35733324daf58dae8692eecd819a19e49280113; reglogin_hasopened=1; reglogin_hasopened=1; regtoken=2000; __utma=61349937.1282976385.1456495741.1456495741.1456495741.1; __utmb=61349937.12.8.1456495791316; __utmc=61349937; __utmz=61349937.1456495741.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1282976385.1456495741; reglogin_isLoginFlag=; reglogin_isLoginFlag=",
            "DNT":"1",
            "Host":"justinbieber520.lofter.com",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
            
            }


    count = 0;
    page = 2; 




    def __init__(self):
        info('init start')
        return

    def start_requests(self): 
        info("start url:"+ self.start_urls[0])
        yield
        scrapy.Request(url=self.start_urls[0],callback=self.parse_pic);


    def parse_pic(self,response):
        info("pic page url:"+ response.url);
        selectorList = response.xpath("//img[@class]/text()")
        for   selector in selectorList:

            link = selector.extract()
            url = str(link.extract())
            info("pic url:"+url)
            yield  scrapy.Request(url=url,callback=self.save_pic)
        next_url =  start_urls[0] + "?page=" + self.page;
        self.page = self.page + 1
        #yield scrapy.Request(url=next_url, callback=self.parse_pic,headers = self.headers);    

    def save_pic():
        info("get pic url:"+url)
        item = LofterItem()
        item["url"] = response.url
        item["content"] = response.body
        item["name"] = self.count
        self.count = self.count + 1
        return item




    def _process_request(self, request):
        info('process ' + str(request))
        return request

