# Diario Oficial

Criando o projeto


scrapy genspider diario https://ww2.tjmsp.jus.br/p_adv0.htm


site:  https://ww2.tjmsp.jus.br/p_processos.htm



scrapy shell 

fetch('https://ww2.tjmsp.jus.br/p_processos.htm')

<200 https://ww2.tjmsp.jus.br/p_processos.htm>


fetch('https://ww2.tjmsp.jus.br/p_adv0.htm')

<200 https://ww2.tjmsp.jus.br/p_adv0.htm>


scrapy crawl diario -o ../data/diario.json