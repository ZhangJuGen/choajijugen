# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:demo.py
@time:2024/11/07
"""
import random

import pytesseract
import requests
from PIL import Image
import io
from ddddocr import DdddOcr
from aip import AipOcr

if __name__ == '__main__':
    # 初始化AipOcr对象
    # APP_ID = '116219984'
    # API_KEY = '8oLdcO130SR4HeQISvh3r9uB'
    # SECRET_KEY = 'q0tIlMax4avDtEVOs5n2644AIbUGdcPA'
    # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # print(len(random.sample(range(1000), 100)))
    res = requests.get("http://123.60.208.194:8580/national-culture-cloud-mrp/c"
                       "aptcha/getCaptcha?r=1731405199108")
    # 获取接口返回的二进制
    image_data = res.content
    # 将二进制转换为图片对象
    image_bytes = io.BytesIO(image_data)
    image = Image.open(image_bytes)
    # 保存图片
    image.save('output.png', 'PNG')
    # 简单的灰度化和二值化处理（可选）
    # image = image.convert('L')  # 转换为灰度图
    # image = image.point(lambda x: 0 if x < 128 else 255, '1')  # 二值化
    # 识别图形验证码
    # text = pytesseract.image_to_string(image)
    # print(text)
    # 识别图形验证码
    result = DdddOcr().classification(image)
    print(result, res.cookies.get('authCode'))
    # with open('output.png', 'rb') as f :
    #     image = f.read()
    # options = {}
    # result = client.basicGeneral(image, options)
    # print(result)
