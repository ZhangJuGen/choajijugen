"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/1/13 0013 下午 4:33
@Auth ： 最下级测试工程师
@File ：get_conf.py
@IDE ：PyCharm
"""
import os

from conf import config
from common.yaml_handle import get_yaml


class Get_Conf:
    """
    获取配置
    """
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.env = config.ENV

    # 获取测试环境
    def get_env(self):
        env = get_yaml(self.env)
        return env["host"][env["default"]]


get_conf = Get_Conf()

if __name__ == '__main__':
    print(get_conf.get_env())
