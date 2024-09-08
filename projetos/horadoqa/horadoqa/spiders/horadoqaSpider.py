import scrapy

class HoradoqaspiderSpider(scrapy.Spider):
    name = "horadoqaSpider"
    allowed_domains = ["horadoqa.github.io"]
    start_urls = ["https://horadoqa.github.io/site/"]

    def parse(self, response):
        
        yield {
            'Título': response.css('h1::text').get()
        }
