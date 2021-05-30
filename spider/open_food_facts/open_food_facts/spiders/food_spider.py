import scrapy


 # the way to use scrapy css please check "https://blog.csdn.net/dangsh_/article/details/78617178"
 # scrapy crawl food -O food.json       ------to start


class FoodSpider(scrapy.Spider):
    name = "food"

    def start_requests(self):
        urls = [
            'https://world.openfoodfacts.org/1',
            'https://world.openfoodfacts.org/2',
            'https://world.openfoodfacts.org/3',
            'https://world.openfoodfacts.org/4',
            'https://world.openfoodfacts.org/5',
            'https://world.openfoodfacts.org/6',
            'https://world.openfoodfacts.org/7',
            # https://world.openfoodfacts.org/product/3274080005003/spring-water-cristaline
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if 'Open Food Facts - World' not in response.css('title::text').get():
            name = response.css("h1::text").get()
            brand = response.css("div.row div.medium-12 p a[itemprop]::text").get()
            category = response.css("div.row div.medium-12 p a[href*='/category']::text").getall()
            carbohydrate = response.css("tr#nutriment_carbohydrates_tr td.nutriment_value::text").get()
            fat = response.css("tr#nutriment_fat_tr td.nutriment_value::text").get()
            sugar = response.css("tr#nutriment_sugars_tr td.nutriment_value::text").get()
            energy = response.css("tr#nutriment_energy-kcal_tr td.nutriment_value::text").get()
            protein = response.css("tr#nutriment_proteins_tr td.nutriment_value::text").get()
            yield {
                'name': name,
                'brand': brand,
                'category': category,
                'carbohydrate': carbohydrate,
                'fat': fat,
                'sugar': sugar,
                'energy': energy,
                'protein': protein,
            }

        else:

            food_pages = response.css("div#search_results li a::attr(href)").getall()

            for food_page in food_pages:
                food_page = response.urljoin(food_page)
                yield scrapy.Request(food_page, callback=self.parse)
