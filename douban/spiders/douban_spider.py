# -*- coding: utf-8 -*-
# Created by Carl on 2/13/2019
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口URL
    start_urls = ['https://movie.douban.com/top250']

    # 默认的解析方法
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")

        # 循环条目
        for i_item in movie_list:
            # 导入定义好的item信息
            douban_item=DoubanItem()
            # 写详细的xpath信息
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            # 数据处理
            for c in content:
                douban_item['year_country_type'] = ''.join(c.split())
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            # 详细页面规则
            detail_link = i_item.xpath(".//a/@href").extract_first()
            yield scrapy.Request(detail_link, callback=self.parse_detail, meta=({'douban_item': douban_item}))
            # 将item信息yield到piplines里面
            # yield douban_item
        # 解析下一页规则，后页的xpath
        # next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)

    def parse_detail(self, response):
        douban_item = response.meta['douban_item']
        douban_item['movie_name'] = response.xpath("//div[@id='content']/h1/span[1]/text()").extract_first()
        douban_item['director_name'] = response.xpath("//div[@id='info']//span[1]//span[2]/a/text()").extract_first()
        writers = response.xpath("//div[@id='info']//span[2]//span[@class='attrs']/a/text()").extract()
        for w in writers:
            douban_item['writer_name'] = '/'.join(w.split())
        # douban_item['starring'] = response.xpath("//span[@class='actor']/span/span/a/text()").extract_first()
        # print(douban_item['starring'])
        # for a in actors:
        # douban_item['starring'] = actors
        # douban_item['language'] = response.xpath("//*[@id='info']/text()[3]").extract()
        date = response.xpath("//span[@property='v:initialReleaseDate']/text()").extract()
        for d in date:
            douban_item['release_date'] = ''.join(d)
        douban_item['film_length'] = response.xpath("//span[@property='v:runtime']/text()").extract_first()
        # douban_item['other_name'] = response.xpath("//*[@id='info']/text()[5]").extract_first()
        douban_item['imdb_link'] = response.xpath("//*[@id='info']/a/text()").extract_first()
        douban_item['introduce'] = response.xpath("//span[@property='v:summary']/text()").extract_first()
        yield douban_item



