import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class GeturlsSpider(CrawlSpider):
    name = 'dihkUrls'
    allowed_domains = ['dihk.de']
    start_urls = ['https://www.ahk.de/en/here-you-find-us']

    rules = (Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),)




    def parse_item(self, response):
        urls = response.url
        urls = str(urls)
        urlDict = dict(dihkUrls=urls)
        with open('dihkurls_findus.json','a+') as f:
            json.dump(urlDict,f)


# 'https://www.ahk.de/en/here-you-find-us',
# 'https://www.dihk.de/de/ueber-uns/die-ihk-organisation/dihk-deinternational-gmbh-12906/'