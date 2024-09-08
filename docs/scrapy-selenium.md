# Scrapy com Selenium

## Instale o Scrapy e Selenium:

```bash
pip install scrapy-selenium
pip install webdriver-manager
pip install chromedriver-py
```

## Configure o Selenium dentro do Scrapy:

No seu arquivo `settings.py` do Scrapy, adicione o seguinte:

from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # Para rodar em modo headless

scrapy crawl mercadolivre -o /../data/diario.json