# HoradoQA

## Criandoo projeto

```bash
scrapy startproject horadoqa 
```

## Criando Spider

```bash
scrapy genspider horadoqaSpider https://horadoqa.github.io/site/
```

fetch('https://horadoqa.github.io/site/')

response
Out[2]: <200 https://horadoqa.github.io/site/>

## Response text

```bash
response.text
```

## Buscando por uma informação específica

Indicando o elemento html e a class

```bash
response.css('h1::text').get()
```

Contando elementos

len(response.css('h1'))

## Executando

scrapy crawl horadoqaSpider -o ./data/horadoqaSpider.json
