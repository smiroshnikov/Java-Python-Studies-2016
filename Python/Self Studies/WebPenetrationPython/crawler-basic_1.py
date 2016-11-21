# idea is to "map" build a catalogue of application resources
from scrapy import Selector  # extracts data using xpath
from scrapy.spiders import BaseSpider  # basic crawling class


class MySpider((BaseSpider)):
    name = "basic_crawler"
    allowed_domains = ['packtpub.com']
    start_urls = ["https://www.packtpub.com"]

    @staticmethod
    def parse(response):
        hxs = Selector(response)
        book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extend()
