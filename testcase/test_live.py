# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:test_live.py
@time:2024/11/18
"""
import pytest
from base.base_api import api_requests


select_live ={
        "method": "post",
        "url": "http://123.60.208.194:8580/national-culture-cloud-mrp/res/live/listResLive",
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


class Test_live:
    def test_search_live(self, login):
        res = api_requests.base_request(select_live)
        print(res.json())


if __name__ == '__main__':
    pass
