import scrapy


class TryoutSpider(scrapy.Spider):
    name = "tryout"
    start_urls = [
        "https://https://blog.scrapinghub.com/1/",
        "https://https://blog.scrapinghub.com/2/",
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = "tryout-%s.html" % page
        with open(filename, "wb") as f:
            f.write(response.body)
