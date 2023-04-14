# Importing required modules
import scrapy

# Defining class MuzeoSpider which inherits the class Spider from scrapy
class MuzeoSpider(scrapy.Spider):
    name = "muzeo"
    allowed_domains = ["fr.muzeo.com"]
    start_urls = ["http://fr.muzeo.com/"]

    def parse(self, response):
        pass
