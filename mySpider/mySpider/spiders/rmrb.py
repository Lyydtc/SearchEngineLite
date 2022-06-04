import scrapy
import datetime as dt


# clean the string
def clean(content):
    return content.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(u'\xa0', '').replace(' ', '')


class RmrbSpider(scrapy.Spider):
    name = 'rmrb'
    allowed_domains = ['paper.people.com.cn']

    # start_urls = ['http://paper.people.com.cn/']
    # examples of links:
    # http://paper.people.com.cn/rmrb/html/2022-06/04/nw.D110000renmrb_20220604_1-01.htm
    # http://paper.people.com.cn/rmrb/html/2022-06/02/nw.D110000renmrb_20220602_1-01.htm
    def start_requests(self):
        urls = []
        # get the urls of the past i days' news
        today = dt.date.today()
        for i in range(100):
            date = (today - dt.timedelta(days=i)).strftime("%Y%m%d")
            for j in range(1, 6):
                urls.append("http://paper.people.com.cn/rmrb/html/" + date[0:4] + "-" + date[4:6] + "/" + date[6:8] +
                            "/nw.D110000renmrb_" + date + "_" + str(j) + "-01.htm")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for news in response.css('div.article'):
            if news.css('h1::text').get() is not None:
                yield {
                    'url': response.url,
                    'title': news.css('h1::text').get(),
                    'news_content': clean(''.join(news.css('p::text').getall()))
                }
