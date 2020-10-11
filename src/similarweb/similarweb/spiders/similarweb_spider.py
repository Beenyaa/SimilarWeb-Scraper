# -*- coding: utf-8 -*-
import scrapy


class SimilarwebSpiderSpider(scrapy.Spider):
    name = 'similarweb_spider'
    allowed_domains = ['https://www.similarweb.com/']
    start_urls = ['https://www.similarweb.com//']

    def parse(self, response):
        pass
