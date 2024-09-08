import scrapy

class MercadoLivreSpider(scrapy.Spider):
    
    name = 'mercadolivre-brand'
    start_urls = ['https://lista.mercadolivre.com.br/tenis-corrida-masculino']

    def parse(self, response):
        
        products = response.css('div.ui-search-result__content')

        for product in products:
            
            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()
            }

# scrapy crawl mercadolivre-brand -o brand.json
# scrapy crawl mercadolivre-brand -o ../../../../data/brand.json