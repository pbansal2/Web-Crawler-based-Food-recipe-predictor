import csv
import scrapy

urls = []
RecIngredient = []
class RecipeSpider(scrapy.Spider):
    name = "recipe_crawler"
    start_urls = ['https://www.epicurious.com/holidays-events/vegetarian-easter-recipes-gallery']

    def parse(self, response):
        for href in response.css("div.gallery-slide-caption__dek-container a::attr(href)").extract():
            urls.append(href)
        # print(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parser)

    def parser(self, response):
        name = response.css('h1 ::text').extract()
        # ingredients = response.css('div.ingredients-info li ::text()').extract()
        print(name)
        # print(ingredients)
        for ingredient in response.css("div.ingredients-info"):
            print(ingredient.xpath('.//ol/li/ul/li/text()').extract())



