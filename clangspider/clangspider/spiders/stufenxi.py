import scrapy


class StufenxiSpider(scrapy.Spider):
    name = 'stufenxi'
    allowed_domains = ['47.95.10.46']
    start_urls = ['http://47.95.10.46/']

    def parse(self, response):
        pass
