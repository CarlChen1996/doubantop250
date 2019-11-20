# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影名
    movie_name=scrapy.Field()
    #导演
    director_name=scrapy.Field()
    #编剧
    writer_name=scrapy.Field()
    #主演
    # starring=scrapy.Field()
    #类别
    # movie_type=scrapy.Field()
    #制片国家地区
    year_country_type = scrapy.Field()
    #语言
    # language=scrapy.Field()
    #上映日期
    release_date=scrapy.Field()
    #片长
    film_length=scrapy.Field()
    #别名
    # other_name=scrapy.Field()
    #IMDb链接
    imdb_link=scrapy.Field()
    #简介
    introduce=scrapy.Field()
    #评价
    evaluate=scrapy.Field()
    #描述
    describe=scrapy.Field()
    #序号
    serial_number=scrapy.Field()
    #评分
    star = scrapy.Field()