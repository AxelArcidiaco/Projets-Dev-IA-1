# Importing the necessary modules
import scrapy

# Defining a new spider by inheriting from scrapy.Spider class
class QuotesSpider(scrapy.Spider):
    name = "quotes" # Name of the spider
    # List of URLs to be crawled
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    # Function to parse the response received from the URLs
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }