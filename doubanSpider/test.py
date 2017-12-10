# -*- coding: utf-8 -*-
from pipelines import DoubanspiderPipeline
from items import DoubanspiderItem

#测试是值否插入数据库
def test():
    item = DoubanspiderItem()
    item['film_name'] = "电影名称"
    item['film_director'] = '电影导演'
    item['film_writer'] = '电影编剧'
    item['film_roles'] = '电影演员'
    item['film_language'] = '电影语言'
    item['film_date'] = '电影上映时间'
    item['film_long'] = '电影时长 **分钟'
    item['film_description'] = '电影描述'
    pipline = DoubanspiderPipeline()
    pipline.process_item(item=item, spider=None)

if __name__ == '__main__':
    test()