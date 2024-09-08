# web Scraping

Pipeline ETL Python

## Monitoramento de Preços de Commodities com SQL e dbt-core (Data Warehouse)

- Python
- [Scrapy Framework](https://scrapy.org/)
- Pandas
- SQL
- Stremlit
- Dashboard

URL: https://lista.mercadolivre.com.br/tenis-corrida-masculino

## Objetivo:

Montar estratégia de Pricing

- Quais marcas são mais encontradas até 10 página
- Qual o preço médio por marca
- Qua a satisfação por marca

## Estrutura de Diretórios

ScrapyMonitoramentoPreco/
├── scrapy_monitoramento/
│   ├── spiders/
│   │   └── preco_spider.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── transform.py
├── dashboard/
│   ├── app.py
├── requirements.txt
└── README.md

- [scrapy](./docs/scrapy.md)
- [pandas](./docs/pandas.md)
- [dashboard](./docs/dashboard.md)
- [powerbi](./docs/powerbi.md)
- [chomedriver](./docs/webdriver.md)

Repositório: https://lvgalvao.github.io/ScrapyMonitoramentoPreco/