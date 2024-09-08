import scrapy

class GlobospiderSpider(scrapy.Spider):
    name = "home"
    allowed_domains = ["www.globo.com"]
    start_urls = ["https://www.globo.com"]

    def parse(self, response):

        # titulos = response.css('h2.post__title::text')

        # for titulo in titulos:

        yield {
            'Número de Títulos': len(response.css('h2.post__title::text')),
            'Título': response.css('h2.post__title::text').getall()
        }

