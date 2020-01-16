import scrapy



class Atracao(scrapy.Item):
    cidade = scrapy.Field()
    endereco = scrapy.Field()
    dia = scrapy.Field()
    hora = scrapy.Field()
    artista = scrapy.Field()


class ViradaCulturalSpider(scrapy.Spider):
    name = 'virada_cultural'
    start_urls =['http://www.viradacultutalpaulista.ps.gov.br']

    def parse(self, response):
