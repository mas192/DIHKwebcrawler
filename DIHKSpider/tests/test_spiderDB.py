from DIHKSpider.DIHKSpider.spiders.spiderDB import SpiderForDIHKDb
from scrapy.crawler import Crawler
from scrapy.settings import Settings



def test_parse_item():

    spider = SpiderForDIHKDb()
    crawler = Crawler(Settings())
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()


