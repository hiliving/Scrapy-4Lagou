# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from twisted.enterprise import adbapi
import pymysql
from First import settings
from scrapy import log
class FirstPipeline(object):

    def __init__(self):

        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()


    def process_item(self, item, spider):

        try:
            # 插入数据
            # 查重处理
            self.cursor.execute(
                """select * from mybt where downLoadName = %s""",
                item['downLoadName'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition is not None:
                #结果返回，已存在，则不插入
                pass
            else:
                self.cursor.execute(
                    """insert into mybt(movClass, downLoadName, downLoadUrl, mvdesc,downimgurl,downdtitle )
                    value (%s, %s, %s, %s, %s, %s)""",
                    (item['movClass'],
                     item['downLoadName'],
                     item['downLoadUrl'],
                     item['mvdesc'],
                     item['downimgurl'],
                     item['downdtitle']
                     ))
                    # 提交sql语句
                self.connect.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item
