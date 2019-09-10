#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/1/8 23:05
import  requests
import time
import xlwt
import random
from fake_useragent import UserAgent

def get_html():
    # k = 1
    # wb = xlwt.Workbook()
    # table = wb.add_sheet("招聘信息")
    # title = [
    #     "岗位id", "公司全名", "福利待遇", "工作地点", "学历"
    # ]
    # for i in range(len(title)):
    #     table.write(0, i, title[i])
    print("=========================")
    # url = "https://www.lagou.com/jobs/positionAjax.json?"
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
    datas = {

        "first": "false",
        "pn": 1,
        "kd": "python",

    }

    # ua = UserAgent()
    # my_headers = {
    #     # "User-Agent": ua.random,
    #     # "Origin": "https://www.lagou.com",
    #     # "Host": "www.lagou.com",
    #     # "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=",
    #     # "Accept-Language": "zh-CN,zh;q=0.9",
    #     # "Accept": "application/json, text/javascript, */*; q=0.01",
    #     # "Cookie": "WEBTJ-ID=20190108231454-1682e07df9660e-0e48ec021c9012-b781636-1327104-1682e07df97aad; _ga=GA1.2.308613935.1546960495; _gid=GA1.2.1976280725.1546960495; user_trace_token=20190108231454-26e5ef57-1358-11e9-8725-525400f775ce; LGUID=20190108231454-26e5f32d-1358-11e9-8725-525400f775ce; JSESSIONID=ABAAABAAAGGABCBBC858A794CDA50DB6889FC1968BE09D8; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221682e081aca99b-0334b3426bb05c-b781636-1327104-1682e081acb6ce%22%2C%22%24device_id%22%3A%221682e081aca99b-0334b3426bb05c-b781636-1327104-1682e081acb6ce%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LGSID=20190108231623-5c4e2057-1358-11e9-8727-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546960495,1546960584,1546960639; LG_LOGIN_USER_ID=18b7fd5695cad88d62b987cb33c251b8f576263a6081ce70; _putrc=AD0A31E47B6D7D86; login=true; unick=%E8%BF%9E%E6%B5%B7%E5%B3%B0_python%E5%B7%A5%E7%A8%8B%E5%B8%88; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=10; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=4d73dfe72ca85d92e23d712aacd21692; _gat=1; gate_login_token=4a99633bde88296b2750ace0594f2b72d963c0ae15a07680; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546962399; LGRID=20190108234638-95cc39ac-135c-11e9-8739-525400f775ce; SEARCH_ID=565b4a036dd0431db378f657b8a87167"
    #     "Host": "www.lagou.com",
    #     "Connection": "keep-alive",
    #     "Content-Length": "37",
    #     "Origin": "https://www.lagou.com",
    #     "X-Anit-Forge-Code": "0",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Accept": "application/json, text/javascript, */*; q=0.01",
    #     "X-Requested-With": "XMLHttpRequest",
    #     "X-Anit-Forge-Token": "None",
    #     "Referer": "https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Cookie": "WEBTJ-ID=20190108231454-1682e07df9660e-0e48ec021c9012-b781636-1327104-1682e07df97aad; _ga=GA1.2.308613935.1546960495; _gid=GA1.2.1976280725.1546960495; user_trace_token=20190108231454-26e5ef57-1358-11e9-8725-525400f775ce; LGUID=20190108231454-26e5f32d-1358-11e9-8725-525400f775ce; JSESSIONID=ABAAABAAAGGABCBBC858A794CDA50DB6889FC1968BE09D8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221682e081aca99b-0334b3426bb05c-b781636-1327104-1682e081acb6ce%22%2C%22%24device_id%22%3A%221682e081aca99b-0334b3426bb05c-b781636-1327104-1682e081acb6ce%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546960495,1546960584,1546960639; LG_LOGIN_USER_ID=18b7fd5695cad88d62b987cb33c251b8f576263a6081ce70; _putrc=AD0A31E47B6D7D86; login=true; unick=%E8%BF%9E%E6%B5%B7%E5%B3%B0_python%E5%B7%A5%E7%A8%8B%E5%B8%88; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=10; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=669f281f6b1aeca464d5c60a370c32ad; gate_login_token=a11478c8fe501c69e912737e89ab20d0490d3d10fce3e182; _gat=1; LGSID=20190109002951-9f67c7fa-1362-11e9-875f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546964995; LGRID=20190109002954-a12a4a13-1362-11e9-875f-525400f775ce; SEARCH_ID=725a902ab00f47ec9c5b6cdaa3a135db"
    # }
    headers = {
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.8",
        # "Host": "www.lagou.com",
        # "X-Requested-With": "XMLHttpRequest",
        # "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_Python%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    }
    # time.sleep(2 + random.randint(0, 2))
    print("start ---------")
    # proxies = {
    #     "https": "https://183.63.123.3:56489",
    # }
    s = requests.Session()
    s.headers.update(headers)
    s.get("https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=")
    content = s.post(url, data=datas)
    print(content.status_code)
    print(content.text)

get_html()