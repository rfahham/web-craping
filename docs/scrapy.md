# Scrapy

Ler documentação - https://scrapy.org/

## Isolando o ambiente

```bash
python3 -m venv ./venv && source venv/bin/activate
```

## Instalar

```bash
pip install scrapy
```

## Criando projeto

```bash
scrapy startproject <nome do projeto>
```

```bash
scrapy genspider mercadolivre https://lista.mercadolivre.com.br/tenis-corrida-masculino
```

## Terminal

Alguns sites possuem bloqueios para WEB SCRAPING

```bash
fetch('https://lista.mercadolivre.com.br/tenis-corrida-masculino')
2024-09-06 15:36:57 [scrapy.core.engine] DEBUG: Crawled (403) <GET https://lista.mercadolivre.com.br/tenis-corrida-masculino> (referer: None)
```

## Para passar por esse bloqueio

Precisa executar o `scrapy shell` na mesma pasta que tenha o settings.py por causa do user agent

```bash
scrapy shell 

fetch('https://lista.mercadolivre.com.br/tenis-corrida-masculino')

2024-09-06 15:39:29 [scrapy.core.engine] INFO: Spider opened
2024-09-06 15:39:31 [urllib3.connectionpool] DEBUG: Starting new HTTPS connection (1): publicsuffix.org:443
2024-09-06 15:39:31 [urllib3.connectionpool] DEBUG: https://publicsuffix.org:443 "GET /list/public_suffix_list.dat HTTP/11" 200 86854
2024-09-06 15:39:31 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://lista.mercadolivre.com.br/tenis-corrida-masculino> (referer: None)
```

## Outro exemplo

```bash
fetch('https://www.globo.com')
2024-09-06 15:44:24 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.globo.com> (referer: None)
```

## Response da requisição

```bash
response
<200 https://www.globo.com>

response
<200 https://lista.mercadolivre.com.br/tenis-corrida-masculino>
```

## Response text

```bash
response.text
```

## Buscando por uma informação específica

Indicando o elemento html e a class

```bash
response.css('div.ui-search-result__content')
```

Contando o número de objetos encontrados

```bash
len(response.css('div.ui-search-result__content'))

57
```

## Criando uma variável com o response

```bash
products = response.css('div.ui-search-result__content')

products

len(products)
57
```
## Verificando a quantidade de objetos

```bash
len(products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element'))
```

## Buscando a Linha

```bash
products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element').get()
'<span class="ui-search-item__brand-discoverability ui-search-item__group__element">MIZUNO</span>'
```

## Buscando somente o nome do fabricante

```bash
products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()
'MIZUNO'
```


## Script do Scrapy

```bash
cd src/coleta/coleta/spiders

scrapy crawl mercadolivre -o ../../../../data/brand.json
```