import scrapy
from craigslist.items import CraigslistItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs


class CLSpider(CrawlSpider):

	name = 'clCrawl'
	allowed_domains = ["craigslist.org"]
	start_urls = ["https://sfbay.craigslist.org/search/sfc/sss?query=rv&sort=rel&min_price=1000"]

	#Defining rule to crawl next pages

	#rules=(Rule(LinkExtractor(restrict_xpaths = ['//a[contains(@href,"&pp")]']),follow=True,callback='parse_d'),)
	rules=(Rule(LinkExtractor(restrict_xpaths = ['//a[@class="button next"]']),follow=True,callback='parse_d'),)


	def parse_d(self, response):
		title = response.xpath('//p[@class="result-info"]/a/text()').extract()
		url = response.xpath('//p[@class="result-info"]/a/@href').extract()
		price = response.xpath('//p[@class="result-info"]/span[@class="result-meta"]/span[@class="result-price"]/text()').extract()


		for title, url, price in zip(title, url, price):
			item = CraigslistItem()
			item['title'] = title
			item['url'] = url
			item['price'] = price
			yield item



