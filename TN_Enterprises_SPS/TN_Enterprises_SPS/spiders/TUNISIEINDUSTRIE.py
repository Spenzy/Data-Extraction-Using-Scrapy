import scrapy


class TunIndSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://www.tunisieindustrie.nat.tn/en/dbs.asp',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@class="table table-striped"]//tbody/tr/td'):
            yield {
                'first' : row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle' : row.xpath('td[3]//text()').extract_first(),