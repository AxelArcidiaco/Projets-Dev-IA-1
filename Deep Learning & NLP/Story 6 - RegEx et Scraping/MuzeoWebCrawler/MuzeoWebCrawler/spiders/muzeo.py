# Importing required modules
import scrapy

# Defining class MuzeoSpider which inherits the class Spider from scrapy
class MuzeoSpider(scrapy.Spider):
    # define the name and start URLs for the spider
    name = "muzeo"
    allowed_domains = ["fr.muzeo.com"]
    start_urls = ["https://fr.muzeo.com/"]

    # define a method to parse the response
    def parse(self, response):
        pass