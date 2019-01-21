#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests
import json
import pymysql
import re
from datetime import datetime
from jingdata_spider import getJingData

def get_index_data(finance_data):
    id = int(finance_data['id'])
    url = "https://insight.jingdata.com/api/company/index?cid={}".format(id)
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'content-type': 'application/json;charset=utf-8',
    }
    html = requests.get(url=url,headers=header)
    print(html.text)

if __name__ == "__main__":
    i = 1
    page_size = 20
    while i<2:
        print("---curpage:{}---".format(i))
        data_list = getJingData(i, page_size)
        if not data_list:
            break
        for finance_data in data_list:
            get_index_data(finance_data)
        i += 1

