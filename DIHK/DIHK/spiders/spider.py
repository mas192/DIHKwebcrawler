import scrapy
import json

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['dihk.de']
    start_urls = ['https://www.dihk.de/de/ueber-uns/die-ihk-organisation/dihk-deinternational-gmbh-12906/',
                  'https://www.dihk.de/de/themen-und-positionen/recht-in-der-wirtschaft/vergaberecht',
                  'https://www.dihk.de/de/themen-und-positionen/recht-in-der-wirtschaft/sicherheit-in-der-wirtschaft',
                  'https://www.dihk.de/de/themen-und-positionen/wirtschaft-digital',
                  'https://www.dihk.de/de/themen-und-positionen/recht-in-der-wirtschaft/datenschutzrecht']



    def parse(self, response):

        # contacts = response.css('div.teaser-contact__content').getall()
        # print(contacts[0])
        # print(contacts[1])



        name = response.css('span.teaser-contact__contact-name::text').getall()
        title = response.css('span.teaser-contact__contact-title::text').getall()
        ntDict = dict(Name=name,
                              Title=title)


        phone = response.css('a.teaser-contact__info-telephone::text').getall()
        email = response.css('a.teaser-contact__info-email::text').getall()
        peDict = dict(Phone=phone,Email=email)
        ntDict.update(peDict)
        print(ntDict)
        with open('contacts.json','a+') as f:
            json.dump(ntDict,f)





# <div class="teaser-contact__contact">
# <span class="teaser-contact__contact-name">Benjamin Leipold</span>
# <span class="teaser-contact__contact-title">Geschäftsführer DIHK DEinternational GmbH</span>
# </div>
#
#
# <div class="teaser-contact__content">
# <div class="teaser-contact__contact">
# <span class="teaser-contact__contact-name">Benjamin Leipold</span>
# <span class="teaser-contact__contact-title">Geschäftsführer DIHK DEinternational GmbH</span>
# </div>
# <div class="teaser-contact__info">
# <a href="tel:+4930203082400" class="teaser-contact__info-telephone">+49 30 20308 2400</a>
# <a href="mailto:leipold.benjamin@dihk.de" class="teaser-contact__info-email">leipold.benjamin@dihk.de</a>
# </div>
# </div>
#
#
# <div class="teaser-contact__info">
# <a href="tel:+4930203082400" class="teaser-contact__info-telephone">+49 30 20308 2400</a>
# <a href="mailto:leipold.benjamin@dihk.de" class="teaser-contact__info-email">leipold.benjamin@dihk.de</a>
# </div>
# </div>
# </div>