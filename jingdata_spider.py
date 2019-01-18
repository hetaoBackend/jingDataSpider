#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests
import json


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
    print(html.text)
    first_res = json.loads(html.text.strip())
    ## data_list is the jingData info, is a list of dict
    data_list = first_res['data']
    return data_list

# ToDo:you should construct the database && write the useful data to database

if __name__ == "__main__":
    i = 1
    page_size = 20
    while i:
        data_list = getJingData(i, page_size)
        if not data_list:
            break
        print(data_list)
        i += 1

