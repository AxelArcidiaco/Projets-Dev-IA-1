# import the string and scrapy modules
import string
import scrapy
from scrapy import Request

# define a class called MangaBaseSpider that extends scrapy.Spider
class MangaBaseSpider(scrapy.Spider):

    # define the name and start URLs for the spider
    name = "Manga"
    start_urls = ['https://myanimelist.net/manga.php']

    # define a method to parse the response
    def parse(self, response):
        # set the xpath expression to select links to other pages
        xp = "//div[@id='horiznav_nav']//li/a/@href"
        # return a generator of Requests to scrape the manga list pages
        return (Request(url, callback=self.parse_manga_list_page) for url in response.xpath(xp).extract())

    # define a method to parse the manga list page
    def parse_manga_list_page(self, response):
        # select all table rows that come after the second row
        for tr_sel in response.css('div.js-categories-seasonal tr ~ tr'):
            # yield a dictionary of information about the manga
            yield {
                "title":  tr_sel.css('a[id] strong::text').extract_first().strip(),
                "synopsis": tr_sel.css("div.pt4::text").extract_first(),
                "type_": tr_sel.css('td:nth-child(3)::text').extract_first().strip(),
                "episodes": tr_sel.css('td:nth-child(4)::text').extract_first().strip(), 
                "rating": tr_sel.css('td:nth-child(5)::text').extract_first().strip()
            }

        # select all links to other pages and generate Requests to scrape them
        next_urls = response.xpath("//div[@class='spaceit']//a/@href").extract()
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)
