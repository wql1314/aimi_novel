import scrapy
from novel.items import NovelItem


class NovelsSpider(scrapy.Spider):
    name = 'novels'
    allowed_domains = ['www.amxsw.com']
    start_urls = ['https://www.amxsw.com/am/sort01/']
    page = 1
    url = 'https://www.amxsw.com/sort/1/{}.html'

    def parse(self, response):
        novel_url_list = response.xpath('//div[@class="fl_right"]/div/h3/a/@href').extract()

        for href in novel_url_list:
            yield scrapy.Request(url=href, callback=self.parse_detail)

        if self.page <= 1018:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse_detail(self, response):
        item = NovelItem()
        print(response.url)

        novel_title = response.xpath('//div[@class="introduce"]/h1/text()').extract()[0]
        novel_time = response.xpath('//div[@class="introduce"]/p[2]/span[1]/text()').extract()[0]
        novel_name = response.xpath('//div[@class="introduce"]/p[2]/span[2]/a/text()').extract()[0]
        novel_state = response.xpath('//div[@class="introduce"]/p[2]/span[3]/text()').extract()[0]
        novel_brief_introduction = response.xpath('//p[@class="jj"]/text()').extract()[0]

        novel_urls = response.xpath('//div[@class="ml_list"]/ul/li')
        try:
            novel_url = novel_urls.xpath('./a/@href').extract()
            chapter_name = novel_urls.xpath('./a/text()').extract()
        except:
            novel_url = novel_urls.xpath('./b/@onclick').extract().repacle("window.open('","").replace("')", "")
            chapter_name = novel_urls.xpath('./b/text()').extract()

        # print(novel_url)
        # print(chapter_name)


        item['novel_title'] = novel_title
        item['novel_time'] = novel_time
        item['novel_name'] = novel_name
        item['novel_state'] = novel_state
        item['novel_brief_introduction'] = novel_brief_introduction
        item['novel_url'] = response.url
        # item['chapter_name'] = chapter_name

        yield item

# //span[@id="articlecontent"]/text()