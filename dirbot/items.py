import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    comments = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
