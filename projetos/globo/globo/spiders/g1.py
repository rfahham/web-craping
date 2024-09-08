import scrapy

class GlobospiderSpider(scrapy.Spider):
    name = "g1"
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com"]
    page_count = 1
    max_pages = 10

    # def parse(self, response):

    #         yield {
    #             'Total de Títulos': len(response.css('div.bastian-feed-item').get()),
    #             'Número Chapeus': len(response.css('span.feed-post-header-chapeu')),
    #             'Chapeus': response.css('span.feed-post-header-chapeu::text').getall(),
    #             'Total Notícias': len(response.css('p::text').getall()),
    #             'Notícias': response.css('p::text').getall(),
    #             'Hora da notícia': response.css('span.feed-post-datetime::text').getall(),
    #             'Em': response.css('span.feed-post-metadata-section::text').getall()
    #         }
        
    def parse(self, response):
            
        noticias = (response.css('div.bastian-feed-item').getall())
            
        for noticia in noticias:

            yield {
                'noticiaa': noticia,
                # 'chapeu': noticia.css('span.feed-post-header-chapeu').get(),
                # # 'Notícia': noticia.css('p::text').get(),
                'Hora da notícia': noticia.css('span.feed-post-datetime::text').get(),
                # 'Em': noticia.css('span.feed-post-metadata-section::text').get()
            }

        if self.page_count < self.max_pages:
            self.page_count += 1
            