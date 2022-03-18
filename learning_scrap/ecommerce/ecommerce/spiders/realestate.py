import scrapy

# Importamos nosso objeto item
from ..items import EcommerceItem

class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/d/real-estate/search/rea/']

    # Esse é o método que roda quando este crawler é ativado. Ele pega a URL e roda o parse
    def parse(self, response):

        print('## Iniciando parse ##')

        allAds = response.css("li.result-row")

        for ad in allAds:
            date = ad.css("time::text").get()
            title = ad.css("a.result-title.hdrlnk::text").get()
            price = ad.css("span.result-price::text").get()
            link = ad.css("a::attr(href)").get()

            items = EcommerceItem()

            items['date'] = date
            items['title'] = title
            items['price'] = price
            items['link'] = link

            yield items
