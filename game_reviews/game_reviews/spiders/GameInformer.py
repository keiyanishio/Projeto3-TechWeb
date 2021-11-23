import scrapy


class GameinformerSpider(scrapy.Spider):
    name = 'GameInformer'
    allowed_domains = ['gameinformer.com']
    start_urls = ['http://gameinformer.com/reviews']

    def parse(self, response):
        for link in response.css(".page-title a::attr(href)"):
            link = "http://gameinformer.com"+link.get()
            yield response.follow(link, callback= self.parse_game)

    def parse_game(self, response): 
        yield {
            "titulo":response.css(".gi5-dynamic-token-fieldnode-game-as-title .page-title::text").get(),
            "nota":response.css(".review-summary-score::text").get(),
            "publisher":response.css(".game-details-publisher::text").get(),
            "desenvolvedora":response.css(".game-details-developer::text").get(),
            "lancamento":response.css(".datetime::text").get(),
        }