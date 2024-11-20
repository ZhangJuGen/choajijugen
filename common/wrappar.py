"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/1/13 0013 下午 4:53
@Auth ： 最下级测试工程师
@File ：wrappar.py
@IDE ：PyCharm

"""
import time
from datetime import datetime


def get_time(func):
    # 装饰器函数，用来获取当前时间
    # current_time = datetime.now().strftime(" %Y-%m-%d %H:%M:%S")
    current_time = str(int(time.time()))

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res + current_time

    return wrapper
