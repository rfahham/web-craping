import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MySpider(scrapy.Spider):
    name = 'chatgpt'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://horadoqa.github.io/site/',
            callback=self.parse,
        )

    def parse(self, response):
        # Obtenha o WebDriver do Selenium a partir de response.meta
        driver = response.meta['driver']
        
        # Encontre o elemento <select> e selecione uma opção
        select_element = Select(driver.find_element(By.NAME, '//*[@id="select-itens"]'))
        select_element.select_by_value('//*[@id="select-itens"]/option[1]')  # Selecione por valor
        
        # Opcional: Clique no botão de envio do formulário
        submit_button = driver.find_element(By.XPATH, '/html/body/div/div[4]/form/input[4]')
        submit_button.click()

        # Atualize o response após a interação com o Selenium
        response = scrapy.http.HtmlResponse(
            url=driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
        )

        # Continue o parsing com Scrapy
        self.parse_page(response)

    def parse_page(self, response):
        # Extraia os dados da página carregada
        title = response.xpath('//title/text()').get()
        print(title)