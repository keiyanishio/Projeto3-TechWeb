import scrapy


class GameinformerSpider(scrapy.Spider):
    name = 'GameInformer'
    allowed_domains = ['gameinformer.com']
    start_urls = ['http://gameinformer.com/reviews']

    def parse(self, response):
        for teaser in response.css(".teaser"):
            yield{
                "titulo" : teaser.css(".page-title a::text").get(),
                "nota" : teaser.css(".score::text").get(),
                "link_pagina" : teaser.css(".page-title a::attr(href)").get(),
        }
#response.css(".pager__item .button::attr(href)").get() link para abrir mais reviews