# -*- coding: utf-8 -*-
import scrapy
from First.items import FirstItem

class SecondSpider(scrapy.Spider):
    name = 'second'
    allowed_domains = []
    start_urls = ['https://www.lagou.com/']

    cookie = {
        "JSESSIONID": "ABAAABAAAGGABCB090F51A04758BF627C5C4146A091E618",
        "_ga": "GA1.2.1916147411.1516780498",
        "_gid": "GA1.2.405028378.1516780498",
        "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1516780498",
        "user_trace_token": "20180124155458-df9f65bb-00db-11e8-88b4-525400f775ce",
        "LGUID": "20180124155458-df9f6ba5-00db-11e8-88b4-525400f775ce",
        "X_HTTP_TOKEN": "98a7e947b9cfd07b7373a2d849b3789c",
        "index_location_city": "%E5%85%A8%E5%9B%BD",
        "TG-TRACK-CODE": "index_navigation",
        "LGSID": "20180124175810-15b62bef-00ed-11e8-8e1a-525400f775ce",
        "PRE_UTM": "",
        "PRE_HOST": "",
        "PRE_SITE": "https%3A%2F%2Fwww.lagou.com%2F",
        "PRE_LAND": "https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FJava%2F%3FlabelWords%3Dlabel",
        "_gat": "1",
        "SEARCH_ID": "27bbda4b75b04ff6bbb01d84b48d76c8",
        "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1516788742",
        "LGRID": "20180124181222-1160a244-00ef-11e8-a947-5254005c3644"
    }
    def parse(self, response):
        for item in response.xpath('//div[@class="menu_box"]/div/dl/dd/a'):
            jobClass = item.xpath('text()').extract()
            jobUrl = item.xpath("@href").extract_first()

            oneItem = FirstItem()
            oneItem["jobClass"] =jobClass
            oneItem["jobUrl"] = jobUrl
            for i in range(30):
                jobUrl2 = jobUrl+str(i+1)
                #print(jobUrl2)
                try:
                    yield scrapy.Request(url=jobUrl2, cookies=self.cookie, callback=self.parse_url)
                except:
                    pass



    def parse_url(self,response):
        for sel2 in response.xpath('//ul[@class="item_con_list"]/li'):
            jobName = sel2.xpath('div/div/div/a/h3/text()').extract()
            jobMoney = sel2.xpath('div/div/div/div/span/text()').extract()

            jobNeed = sel2.xpath('div/div/div/div/text()').extract()
            jobNeed = jobNeed[2].strip()

            jobCompany = sel2.xpath('div/div/div/a/text()').extract()
            jobCompany = jobCompany[3].strip()

            jobType = sel2.xpath('div/div/div/text()').extract()
            jobType = jobType[7].strip()

            jobSpesk = sel2.xpath('div[@class="list_item_bot"]/div/text()').extract()
            jobSpesk = jobSpesk[-1].strip()

            Item = FirstItem()
            Item["jobName"] = jobName
            Item["jobMoney"] = jobMoney
            Item["jobNeed"] = jobNeed
            Item["jobCompany"] = jobCompany
            Item["jobType"] = jobType
            Item["jobSpesk"] = jobSpesk
            yield Item