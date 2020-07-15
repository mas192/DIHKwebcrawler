import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import mysql.connector
from mysql.connector import errorcode

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import mysql.connector
from mysql.connector import errorcode

#MySQL Connection
try:
    # mydb and cursor are instance variables
    # use database credentials and name for connections
    mydb = mysql.connector.connect(host='LOCALHOST', user='dihkSpyder', password='dihkSpyder', database='dihk')
    # cursor is used to iterate through the result set obtained from query
    cursor = mydb.cursor(buffered=True)
    # cursor.execute("set names utf8;")
    print("Connected")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


class SpiderForDIHKDb(CrawlSpider):
    name = "dihkDb"
    allowed_domains = ["dihk.de"]
    start_urls = ["https://www.dihk.de/de/ueber-uns/die-ihk-organisation/dihk-deinternational-gmbh-12906"]

    # Storing the URL in a database
    rules = (Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),)

    def parse_item(self, response):
        x = response.url
        y = str(x)
        name = (y)
        print("Value to be inserted is ===> ", y)
        myquery = INSERT
        IGNORE
        INTO
        `DB_NAME`.
        `TABLE_NAME`(`url_name`)
        VALUE("'+y+'");
        '
        cursor.execute(myquery)
        mydb.commit()