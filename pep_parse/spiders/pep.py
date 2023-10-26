import re
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('section#numerical-index td a::attr(href)')
        for peps_link in peps:
            yield response.follow(peps_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().replace('-', '')
        pattern = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'
        number, name = re.search(pattern, title).groups()
        data = {
            'number': number,
            'name': name,
            'status': (
                response.css('dt:contains("Status") + dd').css('abbr::text').get()
            )
        }
        yield PepParseItem(data)
