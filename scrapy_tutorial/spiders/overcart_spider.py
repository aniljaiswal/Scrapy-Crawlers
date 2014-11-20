import scrapy
from scrapy_tutorial.items import ScrapyTutorialItem

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["www.flipkart.com"]

    def start_requests(self):
        for i in xrange(1, 3394, 20):
            yield self.make_requests_from_url("http://www.flipkart.com/mobiles/pr?sid=tyy,4io&start=%d&ajax=true" % i)

    def parse(self, response):
        for item in response.css('div.product-unit'):
            product = ScrapyTutorialItem()
            product['pid'] = item.css('::attr(data-pid)').extract()
            name = item.css('div.pu-title > a::text').extract()
            product['name'] = name[0].strip()
            product['link'] = item.css('div.pu-title > a::attr(href)').extract()
            product['price'] = item.css('div.pu-details.lastUnit > div.pu-price > div > div.pu-final > span::text').extract()
            yield product

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.in"]
    # start_urls = ["http://www.amazon.in/Smartphones-Basic-Mobiles-Accessories/s?ie=UTF8&page=1&rh=n%3A1389432031"]

    def start_requests(self):
        for i in xrange(2, 69):
            yield self.make_requests_from_url("http://www.amazon.in/Smartphones-Basic-Mobiles-Accessories/s?ie=UTF8&page=%d" % (i) +"&rh=n%3A1389432031")

    # def start_requests(self):
    #     for i in xrange(1,69):
    #         yield self.make_requests_from_url("http://www.amazon.in/Smartphones-Basic-Mobiles-Accessories/s?ie=UTF8&page=%d&rh=n:1389432031" % i)
    
    def parse(self, response):
        for item in response.css('#s-results-list-atf > li.s-result-item'):
            product = ScrapyTutorialItem()
            product['pid'] = item.css('::attr(data-asin)').extract()
            product['name'] = item.css('div > div:nth-child(2) > div > a > h2::text').extract()
            product['link'] = item.css('div > div:nth-child(2) > div > a::attr(href)').extract()
            price = item.css('div > div:nth-child(3) > div:nth-child(1) > a > span.a-color-price::text').extract()
            product['price'] = price
            yield product