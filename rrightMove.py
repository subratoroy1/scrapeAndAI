import scrapy
from scrapy.shell import inspect_response
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess 
from scrapy.spiders import Rule,CrawlSpider
import math
import pandas as pd

class RightMoveSpider(CrawlSpider):
    #scrapy.Spider):
    name = 'property data'
    numURLs = 1200#46724
    aRange = range(math.ceil(numURLs/24))
    priceAndPageRanges = [(i,j) for i in range(100) for j in range(41)]
    start_urls = ['https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&' + 
    'maxPrice=' + str((i+1)*10000) + 
    '&minPrice=' + str(i*10000) + 
    '&index=' + str(j*24) +
    '&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords=' 
    for (i,j) in priceAndPageRanges]
    rules = [ Rule(LinkExtractor(allow=r'^https:\/\/www.rightmove.co.uk\/properties\/\d+$'), callback='parse_aPropertyURL') ]

    def getInitialURLs():
        #df = pd.read_csv("Postcode districts.csv")
        #regions = ['City of London' , 'London' , 'West London']
        #postcodes = df[df['Region'].isin(regions)].tolist()
        priceAndPageRanges = [(i,j) for i in range(100) for j in range(41)]
        URLs = ['https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&' + 
        'maxPrice=' + str(i*10000) + 
        '&minPrice=' + str((i+1)*10000) + 
        '&index=' + str(j*24) +
        '&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords=' for (i,j) in priceAndPageRanges]
        return(URLs)


    def parse_aPropertyURL(self,response):
            print(" i am inside a property page")
            #inspect_response(response,self)
            aProperty = {}
            aProperty['url'] = response.url
            numLabels = len(response.css('div[id="root"]').css('div[class="tmJOVKTrHAB4bLpcMjzQ"]::text').getall())
            for i in range(numLabels):
                aProperty[response.css('div[id="root"]').css('div[class="tmJOVKTrHAB4bLpcMjzQ"]::text')[i].get()] = response.css('div[id="root"]').css('div[class="_1fcftXUEbWfJOJzIUeIHKt"]::text')[i].get()
            aProperty['price'] = response.css('div[id="root"]').css('div[class="_1gfnqJ3Vtd1z40MlC0MzXu"]').xpath('span/text()').get()
            aProperty['address'] = response.css('div[id="root"]').css('h1[class="_2uQQ3SV0eMHL1P6t5ZDo2q"]::text').get()
            aProperty['description'] = response.css('div[id="root"]').css('div[class="STw8udCxUaBUMfOOZu0iL _3nPVwR0HZYQah5tkVJHFh5"]')[0].xpath('div').get()
            
            yield aProperty

# enable below to be able to debug as a standalone python script	
#process = CrawlerProcess()
#process.crawl(RightMoveSpider)
#process.start()