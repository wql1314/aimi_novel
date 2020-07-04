# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说书名
    novel_title = scrapy.Field()
    # 更新时间
    novel_time = scrapy.Field()
    # 作者名
    novel_name = scrapy.Field()
    # 跟新状态
    novel_state = scrapy.Field()
    # 简介
    novel_brief_introduction = scrapy.Field()
    # 章节
    chapter_name = scrapy.Field()
    # 内容
    chapter_context = scrapy.Field()
    #
    novel_chapter_name = scrapy.Field()
    # 小说url
    novel_url = scrapy.Field()