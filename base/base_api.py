# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:base_api.py
@time:2024/11/12
"""
import requests

from common import get_captcha


class Base_api:
    def __init__(self):
        self.client = requests.Session()
    # 请求接口

    def base_request(self, req):
        response = self.client.request(**req)
        return response


api_requests = Base_api()


if __name__ == '__main__':
    captcha, authCode = get_captcha.get_captcha()
    login = {
        "method": "post",
        "url": "http://123.60.208.194:8580/national-culture-cloud-mrp/system/user/denglo",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "authCode": authCode
        },
        "data": {
            "mingzi": "zhangganying",
            "mimi": "anlHanlAMDFAMDJ4dA==",
            "phone": "18229790602",
            "captcha": captcha,
            "phoneCaptcha": "666666",
            "rememberme": "1"
        },
        "allow_redirects": False
    }
    select_live ={
        "method": "post",
        "url": "http://123.60.208.194:8580/national-culture-cloud-mrp/res/live/listResLive",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "authCode": authCode
        },
        "data": {
            "resLiveName": '' ,
            "resId": '' ,
            "mliveName": '',
            "category": '',
            "orderNo": '',
            "creatorName": '',
            "organizer": '',
            "status": '',
            "isPublished": '',
            "areaId": '',
            "dataSource": '1',
            "pageSize": 'DIC_PAGESIZE_10',
            "liveLabelNames”：'',"
            "currPage": '1'
        }
    }
    baseapi = Base_api()
    res = baseapi.base_request(login)
    res = baseapi.base_request(select_live)
    print(res.json())