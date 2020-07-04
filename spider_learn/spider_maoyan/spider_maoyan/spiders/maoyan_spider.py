# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider' # 爬虫名，具有唯一性
    allowed_domains = ['maoyan.com'] # 在该域名下进行爬虫
    start_urls = ['https://maoyan.com/board/4?offset=0'] # 爬虫开始网址

    # 解析响应->处理返回的网页数据的
    # response这个形式参数就是网页数据
    def parse(self, response):
        # 提取数据
        selectors = response.xpath('//dl[@class="board-wrapper"]/dd')
        for selector in selectors:
            title = selector.xpath('./a/@title')
            print(title)
            actor = selector.xpath('.//p[@class="star"]/text()').get(default='').strip()
            print(actor)
