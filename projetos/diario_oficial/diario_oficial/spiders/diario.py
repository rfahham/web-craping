import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DiarioSpider(scrapy.Spider):
    name = "diario"

    allowed_domains = ["ww2.tjmsp.jus.br"]
    start_urls = ["https://ww2.tjmsp.jus.br/p_adv0.htm"]

    def start_requests(self):
        yield SeleniumRequest(
            url= "https://ww2.tjmsp.jus.br/p_adv0.htm",
            callback=self.parse,
        )

    def parse(self, response):
        driver = response.meta['driver']
        
        # Clique no botão usando Selenium
        button = driver.find_element_by_xpath('//*[@id="home"]/div[2]/div/div[4]/div[1]/button[1]')
        button.click()

        # Encontre o campo de formulário e insira o dado
        input_field = driver.find_element_by_name('//*[@id="txt_nro_oab"]')
        input_field.send_keys('96259')

        # Encontre o elemento <select> e selecione uma opção
        select_element = Select(driver.find_element(By.NAME, '//*[@id="psq_oab"]/div[4]/div/select'))
        select_element.select_by_value('RJ')  # Selecione por valor

        button = driver.find_element_by_xpath('//*[@id="btn_enviar"]')
        button.click()

        # Aguarde o carregamento e colete os dados
        response = scrapy.http.HtmlResponse(
            url=driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
        )

        # Agora você pode continuar o parsing com o Scrapy
        self.parse_page(response)

    def parse_page(self, response):
        # Continue extraindo os dados com Scrapy
        title = response.xpath('/html/body').get()
        print(title)
