# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:set_message.py
@time:2024/11/18
"""
from datetime import datetime, timedelta
from conf import config
from common import mysql_handelr


def set_message():
    # 获取当前服务器时间，测试环境服务器比正常时间慢了20分钟
    now = datetime.now() - timedelta(minutes=20)
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")
    sql = "insert into sys_message(phone,verifyCode,create_time,device_type,use_status) " \
          "VALUES('{}','{}','{}','{}','{}')".format(config.PHONE, config.VERIFYCODE, now_time, 'DIC_DEVICE_TYPE_1', '0')
    mysql_handelr.execute_sql(sql)
    return config.VERIFYCODE


if __name__ == '__main__':
    print(set_message())
