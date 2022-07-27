import scrapy


class RneSpider(scrapy.Spider):
    name = 'RNE'
    allowed_domains = [
        'www.registre-entreprises.tn',
        'www.e-rne.tn',
    ]
    start_urls = [
        'http://www.registre-entreprises.tn/',
        'https://e-rne.tn/',
    ]

    def parse(self, response):
        for item in response.css('table'):
            yield {
                'title': quote.css('span.text::text').get(),
                'content': quote.css('td.text::text').get(),
            }
