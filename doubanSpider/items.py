#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DoubanspiderItem(Item):
    # 电影名字
    film_name = Field()
    # 电影导演
    film_director = Field()
    # 电影编剧
    film_writer = Field()
    # 电影演员
    film_roles = Field()
    # 电影语言
    film_language = Field()
    # 电影上映时间
    film_date = Field()
    # 电影时长 **分钟
    film_long = Field()
    # 电影描述
    film_description = Field()
