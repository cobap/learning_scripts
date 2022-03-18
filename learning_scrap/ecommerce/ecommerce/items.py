# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Esse daqui será um dos items resultado do scrapy
class EcommerceItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()

