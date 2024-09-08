# Globo

fetch('https://www.globo.com')


## Indicando o elemento html e a class

```bash
len(response.css('h2.post__title'))
```

scrapy crawl globoSpider -o ./data/globo.json

G1

titulos = response.css('p')

len(titulos)

titulos.get()
Out[8]: '<p elementtiming="text-ssr">Brasil avisa que vai representar Argentina até novo país ser escolhido </p>'

In [9]: titulos.getall()
Out[9]: 
['<p elementtiming="text-ssr">Brasil avisa que vai representar Argentina até novo país ser escolhido </p>',
 '<p elementtiming="text-ssr">7 de Setembro: desfile tem representantes dos 3 Poderes, atletas olímpicos e homenagem ao RS</p>',
 '<p elementtiming="text-ssr">Em ato na Paulista, Bolsonaro pede anistia para condenados do 8/1 e chama Alexandre de Moraes de ditador</p>',
 '<p elementtiming="text-ssr">Tarcísio de Freitas e Ricardo Nunes foram ao evento.</p>',
 '<p elementtiming="text-ssr">PM cai do cavalo e morre antes de evento no sambódromo</p>',
 '<p elementtiming="text-ssr">\'The Room Next Door\', de Almodóvar, leva o Leão de Ouro; veja todos vencedores</p>',
 '<p elementtiming="text-ssr">Brasil faz exercício militar conjunto com tropas de China e EUA</p>',
 '<p elementtiming="text-ssr">O ASSUNTO: como e quando a situação de Silvio Almeida ficou insustentável</p>',
 '<p elementtiming="text-ssr">Reunião de Lula com Anielle teve só mulheres como participantes</p>']

 In [11]: titulos.css('p').get()
Out[11]: '<p elementtiming="text-ssr">Brasil avisa que vai representar Argentina até novo país ser escolhido </p>'


In [12]: titulos.css('p::text').get()
Out[12]: 'Brasil avisa que vai representar Argentina até novo país ser escolhido '


Chapeu

response.css('span.feed-post-header-chapeu::text')