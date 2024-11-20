"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/1/13 0013 下午 4:27
@Auth ： 最下级测试工程师
@File ：yaml_handle.py
@IDE ：PyCharm
"""
import yaml
import os

from conf import config
from common.logs import logger


class Yaml_Handle:
    # 获取项目路径
    def __init__(self):
        self.Base_Path = config.BasePath

    # 读取yaml文件
    def get_yaml(self, path):
        dir_name = ''
        file_name = path.split('TestCase')[0]
        # 如果传过来的只有文件名（**.yaml），则默认它的文件夹路径为testCaseAddress
        if os.path.split(path)[0] == '':
            dir_name = config.testCaseAddress

        # 将文件路径拼接起来
        path = os.path.join(self.Base_Path, dir_name, path)

        # 将文件内容读取并转换为字典格式
        with open(path, mode="r+", encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if 'TestCase' in path:
            return data[file_name]
        else:
            return data

    # 将字典数据转换为yaml文件
    def create(self, data):
        # 存放的文件路径
        file_path = os.path.join(self.Base_Path, config.requestAddress,
                                 "new_requests.yaml")

        # 开始转换
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                yaml.safe_dump(data=data,
                               stream=f,
                               default_flow_style=False,
                               encoding='utf-8',
                               allow_unicode=True)
            logger().info("yaml文件转换成功")
        except Exception as e:
            logger().error(e, exc_info=True)


get_yaml = Yaml_Handle().get_yaml
if __name__ == '__main__':
    print(get_yaml("saveExaPlanTestCase.yml"))
