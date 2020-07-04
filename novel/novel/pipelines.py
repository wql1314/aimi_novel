# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class NovelPipeline(object):

    def process_item(self, item, spider):
        return item

class MySQLPipeline(object):

    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'Novels')
        host = spider.settings.get('MYSQL_HOST', '111.229.144.195')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'wang8471268')

        self.db_conn = pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd)

        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self,item,spider):
        self.insert_db(item)
        return item

    def insert_db(self,item):

        values = (
        item['novel_title'],
        item['novel_time'],
        item['novel_name'],
        item['novel_state'],
        item['novel_brief_introduction'],
        item['novel_url'],
        # item['chapter_name'],
        )
        print("#" * 80)

        print(values)

        print("#" * 80)
        try:
            sql = 'insert into novel(novel_title,novel_time,novel_name,novel_state,novel_brief_introduction,novel_url) values (%s,%s,%s,%s,%s,%s)'
            self.db_cur.execute(sql,values)
            self.db_conn.commit()
            print("插入完成")
        except:
            sql = 'insert into novel(novel_title, novel_time, novel_name, novel_state, novel_brief_introduction,novel_url) values (%s,%s,%s,%s,%s,%s)'
            self.db_conn.ping()
            print(sql)
            self.db_cur.execute(sql,values)
            self.db_conn.commit()
            print("插入完成")

        else:
            print("插入出错")
            self.db_conn.ping()
            self.db_conn.commit()
            self.db_conn.close()
