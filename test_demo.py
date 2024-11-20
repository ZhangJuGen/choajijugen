# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:test_demo.py
@time:2024/10/23
"""
import pytest
import requests


class Test_demo:

    def test_clear(self):
        res = requests.get('http://gjpc.hanyastar.cn/api/v1/clearcache')
        print(res.status_code, res.text)
        assert res.status_code == 200

    def test_web(self):
        test_params = {
            'resId': '10731207',
            'topiCid': '386',
            'Org': '1'
        }
        res = requests.get('http://gjh5.hanyastar.cn/thematic/wywhgztzj2024/vote-detail.html', params=test_params)
        print(res.text)


if __name__ == '__main__':
    pass
