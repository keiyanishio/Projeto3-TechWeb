import scrapy


class GameinformerSpider(scrapy.Spider):
    name = 'GameInformer'
    allowed_domains = ['gameinformer.com']
    start_urls = ['http://gameinformer.com/reviews']

    def parse(self, response):
        for link in response.css(".page-title a::attr(href)"):
            link = "http://gameinformer.com"+link.get()
            yield response.follow(link, callback= self.parse_game)
        next_page = response.css(".button::attr(href)").get()
        next_page = "http://gameinformer.com"+next_page
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_game(self, response): 
        yield {
            "titulo":response.css(".gi5-dynamic-token-fieldnode-game-as-title .page-title::text").get(),
            "nota":response.css(".review-summary-score::text").get(),
            "publisher":response.css(".game-details-publisher::text").getall()[1],
            "desenvolvedora":response.css(".game-details-developer::text").getall()[1],
            "lancamento":response.css(".datetime::text").get(),
        }