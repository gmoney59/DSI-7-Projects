import scrapy
from scrapy.loader import ItemLoader
from craigslist.items import CraigslistItem



class CraigslistSpider(scrapy.Spider):
    name = 'brian'
    allowed_domains = ["craigslist.org"]
    start_urls = [
        #"https://sfbay.craigslist.org/search/sfc/rva?query=rv&sort=rel&min_price=1000"
        "https://sfbay.craigslist.org/search/sfc/sss?query=rv&sort=rel&min_price=1000"
    ]

    def parse(self, response):
        title = response.xpath('//p[@class="result-info"]/a/text()').extract()
        url = response.xpath('//p[@class="result-info"]/a/@href').extract()
        price = response.xpath('//p[@class="result-info"]/span[@class="result-meta"]/span[@class="result-price"]/text()').extract()


        for title, url, price in zip(title, url, price):
            item = CraigslistItem()
            item['title'] = title
            item['url'] = url
            item['price'] = price
            yield item



