#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests
import json
import pymysql
import re
from datetime import datetime
from jingdata_spider import getJingData

db = pymysql.connect("localhost", "root", "12345678", "test", charset='utf8')
cursor = db.cursor()

# 插入financing_id表
def insert_finance_id(finance_data):

    sql = """
                INSERT INTO financing_id(`finance_id`, `name`) \
                VALUES ({0}, "{1}")""" \
        .format(finance_data['id'] , finance_data['name'])

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print(sql)
        db.rollback()

if __name__ == "__main__":
    i = 1
    page_size = 20
    while i:
        print("---curpage:{}---".format(i))
        data_list = getJingData(i, page_size)
        if not data_list:
            break
        for finance_data in data_list:
            insert_finance_id(finance_data)
        i += 1
    db.close()

