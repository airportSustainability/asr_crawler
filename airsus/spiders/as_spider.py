import scrapy
import tldextract


class ASRSpider(scrapy.Spider):
    name = "asr_reports"

    def start_requests(self):
        urls = [
            'https://www.eindhovenairport.nl/en/annual-reports',
            # 'https://www.eindhovenairport.nl/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def is_interesting(self, link, link_text, footer_links):
        if link is None or link in footer_links:
            return False
        if link.endswith('.pdf'):
            return True
        if link_text is None:
            return False
        link_text = link_text.lower()
        keywords = ['asr', 'asr report']
        for k in keywords:
            if k in link_text:
                return True
        return False

    def remove_duplicates(self, to_save):
        return [dict(t) for t in {tuple(d.items()) for d in to_save}]

    def parse(self, response):
        anchors = response.css('a')
        footer_links = response.css('footer a::attr(href)').getall()
        to_follow = []
        to_save = []
        domain = tldextract.extract(response.request.url).domain
        for a in anchors:
            link = a.css('::attr(href)').get()
            link_text = a.css('::text').get()
            if self.is_interesting(link, link_text, footer_links):
                to_save.append({
                    'link': link,
                    'link_text': link_text
                })
            elif link is not None and 'mailto' not in link and tldextract.extract(link).domain == domain:
                to_follow.append(link)

        for i in self.remove_duplicates(to_save):
            yield i
        for i in to_follow:
            yield response.follow(i, callback=self.parse)

        self.log(f'Done')
