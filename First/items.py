# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movClass = scrapy.Field()#电影分类
    movUrl = scrapy.Field()#电影分类的URL

    mvName = scrapy.Field()
    mvUrl = scrapy.Field()

    downLoadUrl = scrapy.Field()#下载地址
    downLoadName = scrapy.Field()#下载电影的名称
    downimgurl = scrapy.Field()#电影海报图片
    mvdesc = scrapy.Field()#电影的详情介绍
    downdtitle = scrapy.Field()#下载的电影的标题

