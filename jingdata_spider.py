#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests
import json
import pymysql
import re
from datetime import datetime

db = pymysql.connect("localhost", "root", "12345678", "test", charset='utf8')
cursor = db.cursor()

# get jingData info
def getJingData(page_index, page_size):
    url = 'https://insight.jingdata.com/api/company/search'
    header = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'content-type':'application/json;charset=utf-8',
        # modify the cookie if you log in
        'cookie': 'acw_tc=276aede215478206284705842e0454493a5b1abe829930eb3fb6597d3b9e6e; dfp=SuNYGTvncQFcqrqKn7XZB/lnChY9wVHzeb6JdJODEF8jx7CRAJnEzVuD1EQzHq0nXPSfNv9K6FaHqQotPwiE2Pgx7oLnC6P5b2ihfohLfRTs0+I0QR6EUCrLuZ4j/r9iiD5KZHFNz5Cxo8brtip02xcua+f9SA7A+UY1FZJj4dk%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216537%22%2C%22%24device_id%22%3A%22168614c4eee35a-007649a18cb26d-10306653-1296000-168614c4eef956%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22168614c4eee35a-007649a18cb26d-10306653-1296000-168614c4eef956%22%7D; insight_uid=16537; laravel_session=80rYvckdq4EIyFll3IIAetnSyJbUJZcP2bAXWx4u'
    }
    paramters = {
        'curPage':'{}'.format(page_index),
        'pageSize':'{}'.format(page_size),
        'sort':'[{"field":"market_value","sort":"desc"}]',
        'sub_search':'[]',
        'type':'nq_stock'
    }
    html = requests.post(url=url,params=paramters,headers=header)
    first_res = json.loads(html.text.strip())
    ## data_list is the jingData info, is a list of dict
    data_list = first_res['data']['list']
    return data_list

# ToDo:you should construct the database && write the useful data to database

# 插入financing_data表
def insert_finance(finance_data):

    source_from = "2001-01-01 00:00:00"
    if finance_data['annual_turnover'] and len(finance_data['annual_turnover']['source_from']) > 0:
        date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", finance_data['annual_turnover']['source_from'][0])
        if len(date_all) > 0:
            source_from = date_all[0]

    sql = """
                INSERT INTO financing_data(`name`, `full_name`, `stock_short_name`, `establish_date`,\
                 `market_value`, `industry`, `annual_turnover`, `annual_profit`, \
                 `source_from`, `address`, `operation_tags`,`tags`, `short_description`,\
                  `description`, `finance_phase`, `latest_investment_finance_date`, `total_investors`,\
                  `pe_financing_amount`, `pe_heat_value`, `pe_heat_change_pct`,`ipo_financing_amount`, \
                  `listed_date`, `share_placement_amount`, `total_financing_amount`, `close_price`, \
                  `change_price_pct_1m`, `change_price_pct_3m`, `turnover_volume`, `turnover_value`, \
                  `eps`, `roe`, `pe_ttm`, `ps`, `pb`, `total_shares`, `circulation_shares`) \
                VALUES ("{0}", "{1}", "{2}","{3}",{4},"{5}",{6},{7},"{8}","{9}","{10}","{11}",'{12}','{13}', \
                "{14}","{15}", "{16}",{17}, {18},{19},{20},"{21}",{22},{23},{24},{25},{26},{27},\
                {28},{29},{30},{31},{32},{33},{34},{35})""" \
        .format(finance_data['name'], finance_data['full_name'], finance_data['stock_short_name'], get_date(finance_data['establish_date']), \
                get_value(finance_data['market_value'], "value"), get_value(finance_data['industry'], "label"), get_value(finance_data['annual_turnover'], "value"), \
                get_value(finance_data['annual_profit'], "value"), source_from, finance_data['address'], finance_data['operation_tags'], \
                finance_data['tags'], finance_data['short_description'], finance_data['description'],get_value(finance_data['finance_phase'], "label"), \
                get_date(finance_data['latest_investment_finance_date']), finance_data['total_investors'], get_value(finance_data['pe_financing_amount'], "value"),\
                get_num(finance_data['pe_heat_value']), get_num(finance_data['pe_heat_change_pct']),
                get_value(finance_data['ipo_financing_amount'], "value"), get_date(finance_data['listed_date']),get_value(finance_data['share_placement_amount'], 'value'),\
                get_value(finance_data['total_financing_amount'], 'value'),get_value(finance_data['close_price'], 'value'), \
                get_num(finance_data['change_price_pct_1m']), get_value(finance_data['change_price'], 'value'),\
                get_num(finance_data['change_price_pct_1m']), get_num(finance_data['change_price_pct_3m']), \
                get_num(finance_data['turnover_volume']), get_value(finance_data['turnover_value'], 'value'), \
                get_value(finance_data['eps'], 'value'), get_num(finance_data['roe']), \
                get_num(finance_data['pe_ttm']), get_num(finance_data['ps']), \
                get_num(finance_data['pb']), get_num(finance_data['total_shares']), \
                get_num(finance_data['circulation_shares'])
                )

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print(sql)
        db.rollback()

def get_value(data_dict, key):
    value = "null"
    if data_dict and key in data_dict:
        value = data_dict[key]
    return value

def get_num(raw_num):
    return 'null' if not raw_num else raw_num

def get_date(raw_date):
    return "2001-01-01" if not raw_date else raw_date

if __name__ == "__main__":
    i = 1
    page_size = 20
    while i:
        print("---curpage:{}---".format(i))
        data_list = getJingData(i, page_size)
        if not data_list:
            break
        for finance_data in data_list:
            insert_finance(finance_data)
        i += 1
    db.close()

