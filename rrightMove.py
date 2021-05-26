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
            yield {
                'num_bedrooms': response.xpath('//*[@id="root"]/div/div[4]/main/div[5]/div[2]/div[2]/div[2]/div').get(),
                'property_type': response.xpath('//*[@id="root"]/div/div[4]/main/div[5]/div[1]/div[2]/div[2]/div').get(),

                'test': response.xpath('//*[@id="root"]/div/div[4]/main/div[5]/div[1]/div[2]/div[2]/div/text()').get(),
                
                'size': response.xpath('//*[@id="root"]/div/div[4]/main/div[5]/div[4]/div[2]/div[2]/div[1]').get(),
                'short_description': response.xpath('//*[@id="root"]/div/div[4]/main/div[9]/div/div').get()
            }
	
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()