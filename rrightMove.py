import scrapy
from scrapy.shell import inspect_response
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess 
from scrapy.spiders import Rule,CrawlSpider

class QuotesSpider(CrawlSpider):
    #scrapy.Spider):
    name = 'property data'
    start_urls = [
        'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&index=0&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='
    ]
    rules = [ Rule(LinkExtractor(allow=r'^https:\/\/www.rightmove.co.uk\/properties\/\d+$'), callback='parse_aPropertyURL') ]

    def parse_aPropertyURL(self,response):
            print(" i am inside a property page")
            #inspect_response(response,self)
            numLabels = len(response.css('div[id="root"]').css('div[class="tmJOVKTrHAB4bLpcMjzQ"]::text').getall())
            for i in range(numLabels):
                yield {response.css('div[id="root"]').css('div[class="tmJOVKTrHAB4bLpcMjzQ"]::text')[i].root : 
                        response.css('div[id="root"]').css('div[class="_1fcftXUEbWfJOJzIUeIHKt"]::text')[i].root}
	
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()