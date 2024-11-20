# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:conftest.py
@time:2024/11/18
"""
import pytest
from base.base_api import api_requests
from common import get_captcha, set_message
from conf import config

# 图形验证码
captcha, authCode = get_captcha.get_captcha()

# 用户名和密码
UserName = config.USERNAME
UserPassword = config.USERPASSWORD

# 短信验证码
Message = set_message.set_message()

# 登录接口请求模板
login_data = [{
        "method": "post",
        "url": "http://123.60.208.194:8580/national-culture-cloud-mrp/system/user/denglo",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "authCode": authCode
        },
        "data": {
            "mingzi": UserName,
            "mimi": UserPassword,
            "phone": "18229790602",
            "captcha": captcha,
            "phoneCaptcha": Message,
            "rememberme": "1"
        },
        # 取消重定向
        "allow_redirects": False
    }]


@pytest.fixture(scope='session', params=login_data)
def login(request):
    data = request.param
    res = api_requests.base_request(data)


if __name__ == '__main__':
    pass
