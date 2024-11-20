# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:get_captcha.py
@time:2024/11/13
"""
import time
import requests
from PIL import Image
import io
from ddddocr import DdddOcr


def get_captcha():
    result = '0'
    # 识别验证码直到成功获取
    while len(result) != 4:
        # 获取当前时间戳
        time_stamp = str(int(time.time()))
        # 请求验证码
        res = requests.get("http://123.60.208.194:8580/national-culture-cloud-mrp/c"
                           "aptcha/getCaptcha?r=" + time_stamp)
        # 获取接口返回图片的二进制
        image_data = res.content
        # 将二进制转换为图片对象
        image_bytes = io.BytesIO(image_data)
        image = Image.open(image_bytes)
        # 保存图片
        image.save('../output.png', 'PNG')
        # 识别图形验证码
        result = DdddOcr().classification(image)
        # 返回验证码和cookie
    else:
        return [result, res.cookies.get("authCode")]


if __name__ == '__main__':
    print(get_captcha())
