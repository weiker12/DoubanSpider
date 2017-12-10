#!/usr/bin/env python
# coding: utf-8

from doubanSpider.items import DoubanspiderItem
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class MySpider(BaseSpider):
    name = "doubanSpider"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/subject/26378579/?tag=热门&from=gaia']
    url = 'https://movie.douban.com/subject/26378579/?tag=热门&from=gaia'


    def parse(self, response):
        selector = Selector(response)
        item = DoubanspiderItem()
        item['film_name'] = selector.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0].encode("UTF-8")
        print "item['film_name']: {0}".format(item['film_name'])
        item['film_director'] = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()[0].encode("UTF-8")
        print "item['film_director'] :{0}".format(item['film_director'])
        item['film_writer'] = selector.xpath('//*[@id="info"]/span[2]/span[2]/a[1]/text()').extract()[0].encode("UTF-8")
        print "item['film_writer'] :{0}".format(item['film_writer'])
        item['film_roles'] = selector.xpath('//*[@id="info"]/span[3]/span[1]/text()').extract()[0].encode("UTF-8")
        print "item['film_roles'] :{0}".format(item['film_roles'])
        item['film_language'] = '英语'
        print "item['film_language'] :{0}".format(item['film_language'])
        item['film_date'] = selector.xpath('//*[@id="info"]/span[11]/text()').extract()[0].encode("UTF-8")
        print "item['film_date'] :{0}".format(item['film_date'])
        item['film_long'] = selector.xpath('//*[@id="info"]/span[15]/text()').extract()[0].encode("UTF-8")
        print "item['film_long'] :{0}".format(item['film_long'])
        item['film_description'] = selector.xpath('//*[@id="link-report"]/span[1]/text()').extract()[0].encode("UTF-8").strip()
        print "item['film_description'] :{0}".format(item['film_description'])
        return item
