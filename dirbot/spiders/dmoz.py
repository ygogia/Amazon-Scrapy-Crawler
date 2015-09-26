import scrapy
from dirbot.items import DmozItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
class DmozSpider(CrawlSpider):
    name = "amazon"
    allowed_domains = ["amazon.in"]
    start_urls = [
        "http://www.amazon.in/gp/product/B006OLPCUW/ref=s9_simh_gw_p23_d3_i5?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=center-5&pf_rd_r=1Z0ZSMDATMWZ58S5YBS4&pf_rd_t=101&pf_rd_p=518028627&pf_rd_i=1320006031"
    ]
    rules = [
    Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item')
    ]
    def parse_item(self, response):
        for sel in response.xpath('/html'):
            item = DmozItem()
            item['title'] = sel.xpath('//span[@id="productTitle"]/text()').extract()
            item['price'] = sel.xpath("//span[@class='a-size-medium a-color-price']/text()").extract()
            item['comments'] = sel.xpath('//div[@class="a-section"]/text()').extract()
            item['rating'] = sel.xpath('//div[@id="ratingStars"]/text()').extract()
            yield item
