# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:conftest.py
@time:2022/07/09
"""
import pytest
from common.logs import logger
from common.jsonsearch_handle import json_search
from common.yaml_handle import get_yaml
from base.base_requests import base_requests


test_account = get_yaml("login.yml")["login"]["data"]
ids = get_yaml("login.yml")["login"]["ids"]


@pytest.fixture(scope="session", params=test_account, ids=ids)
def get_token(request):
    try:
        # 获取参数
        data = request.param
        # 登陆
        res = base_requests.parametric_requests(data, "login.yml").json()
        # 判断returnCode是否正确
        assert json_search(res, "returnCode") == 200
        # 读取token
        token = res["data"]["authorizationToken"]
        # 返回token
        yield token
    except AssertionError as e:
        logger("登陆接口").info("登陆接口异常：{}".format(e))
