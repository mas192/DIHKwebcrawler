import scrapy


class GetemailsSpider(scrapy.Spider):
    name = 'getEmails'
    allowed_domains = ['dihk.de']
    start_urls = ['http://https://www.ahk.de/en/here-you-find-us/']

    def parse(self, response):
        pass
