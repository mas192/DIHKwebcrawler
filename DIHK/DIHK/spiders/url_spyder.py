import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json

class SpiderGetUrls(CrawlSpider):
    name = 'dihkUrls'
    allowed_domains = ['dihk.de']
    start_urls = ['https://www.dihk.de/de/ueber-uns/die-ihk-organisation/dihk-deinternational-gmbh-12906/']

    rules = (Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),)





def parse_item(self, response):
    link = response.url
    urls = str(link)
    with open('dihkUrls.json','a') as f:
        json.dump(urls,f)