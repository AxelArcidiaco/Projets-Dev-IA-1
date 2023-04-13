# Importing the necessary modules
from pathlib import Path
import scrapy

# Defining a new spider by inheriting from scrapy.Spider class
class QuotesSpider(scrapy.Spider):
    name = "quotes"  # Name of the spider

    # Function to generate the starting URL requests. This function can be replaced by a list of URLs to be crawled
    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            # Yielding a scrapy.Request object for each URL with a callback to self.parse method
            yield scrapy.Request(url=url, callback=self.parse)

    # Callback function to process the responses
    def parse(self, response):
        page = response.url.split("/")[-2]  # Extracting the page number from the URL
        filename = f'quotes-{page}.html'  # Defining the filename with the page number
        Path(filename).write_bytes(response.body)  # Writing the response content to a file
        self.log(f'Saved file {filename}')  # Logging the filename as a message
