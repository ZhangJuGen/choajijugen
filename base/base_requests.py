"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/1/13 0013 下午 4:22
@Auth ： 最下级测试工程师
@File ：base_requests.py
@IDE ：PyCharm


"""
import json
import requests
import os

from conf import config
from common.get_conf import get_conf
from common.logs import logger
from common.template_handle import handle_template


class Base_Requests:
    """
    调用接口模块
    method:接口类型
    url：接口地址
    **req：打包的接口参数
    """

    def __init__(self):
        self.host = get_conf.get_env()
        self.Base_Path = config.BasePath

    # 调用接口
    def send_requests(self, method, url, req: dict):
        url = self.host + url
        try:
            res = requests.request(method=method, url=url, **req)
            logger().info(
            """
            请求地址：{}  \n
            请求参数：{}  \n
            返回信息: {}  \n
            """ .format(url, req, res.json())
            )
            return res
        except Exception as e:
            logger('调用接口时报错').error(e, exc_info=True)

    # 使用模板调用接口
    def parametric_requests(self, params, path):
        # 如果传过来的只有文件名（**.yaml），则默认它的文件夹路径为requestAddress
        dir_name = ''
        if os.path.split(path)[0] == '':
            dir_name = config.requestAddress

        # 将文件路径拼接起来
        path = os.path.join(self.Base_Path, dir_name, path)
        data = handle_template.template(params, path)
        print(data)
        res = self.send_requests(data["args"][0], data["args"][1], data["kwargs"])
        return res


base_requests = Base_Requests()
if __name__ == '__main__':
    data = yaml_handle.get_yaml("login.yml")["login"]["data"]
    res=base_requests.parametric_requests(data,"login.yml")
    print(res.json()["data"]["authorizationToken"])
    print(res.request.body)
