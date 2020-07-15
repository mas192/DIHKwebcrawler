import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderForDIHK(CrawlSpider):
    name = "DIHK"
    allowed_domains = ["dihk.de"]
    start_urls = ["https://www.dihk.de/de/ueber-uns/die-ihk-organisation/dihk-deinternational-gmbh-12906"]

    rules = (Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),)

    def parse_item(self, response):
        filename = response.url
        file1 = open("file_test.txt", "a+")
        string = str(filename)
        file1.write(string + '\n')
        file1.close()