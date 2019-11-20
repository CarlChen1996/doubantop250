# -*- coding: utf-8 -*-
# Created by Carl on 2/13/2019
from scrapy import cmdline
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
# cmdline.execute("scrapy crawl douban_spider".split())
cmdline.execute("scrapy crawl douban_spider -o douban_top250.csv".split())
