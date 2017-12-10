# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from utils.constant import MYSQL_HOST
from utils.constant import MYSQL_USER_NAME
from utils.constant import MYSQL_PASSWORD
from utils.constant import MYSQL_DBNAME
from utils.db_tool import SqlDB
from items import DoubanspiderItem

class DoubanspiderPipeline(object):

    def __init__(self, db_session=None):
        if db_session is None:
            self.db_session = SqlDB(host=MYSQL_HOST, user=MYSQL_USER_NAME, passwd=MYSQL_PASSWORD, database=MYSQL_DBNAME)

    #保存豆瓣的爬虫数据
    def process_item(self, item, spider):
        if item:
            print "豆瓣爬虫数据落表开始"
            column_list = ('film_name', 'film_director', 'film_writer', 'film_roles', 'film_language', 'film_date', 'film_long', 'film_description')
            value_list = (item['film_name'], item['film_director'], item['film_writer'], item['film_roles'], item['film_language'], item['film_date'], item['film_long'], item['film_description'])
            self.db_session.insert(tablename='douban_film_data', column_list=column_list, value_list=value_list) #将爬虫数据插入数据库
            print "豆瓣爬虫数据落表完成"
        return item
