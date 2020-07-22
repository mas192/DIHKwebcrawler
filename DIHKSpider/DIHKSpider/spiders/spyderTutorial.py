import scrapy


class DIHK(scrapy.Spider):
    name = "trial1"


    start_urls = ["https://www.dihk.de/de/ueber-uns/die-ihk-organisation/dihk-deinternational-gmbh-12906"]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)



        # name_dict = dict(['Name',[]])
        # name = response.css('.teaser-contact__contact-name').getall()
        # name_dict['Name'].append(name)
        # print(name_dict)
        # print(name)