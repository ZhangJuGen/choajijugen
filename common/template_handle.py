"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/1/13 0013 下午 4:27
@Auth ： 最下级测试工程师
@File ：template_handle.py
@IDE ：PyCharm
"""

import yaml
import os
from string import Template

from conf import config
from common.logs import logger


class Handle_templata:
    # 获取当前路径
    def __init__(self):
        self.BasePath = config.BasePath

    # 模板替换，将测试用例中的内容替换到接口模板中，实现数据驱动
    def template(self, data, path):
        dir_name = ''
        # 如果传过来的只有文件名（**.yaml），则默认它的文件夹路径为requestAddress
        if os.path.split(path)[0] == '':
            dir_name = config.requestAddress

        # 将文件路径拼接起来
        path = os.path.join(self.BasePath, dir_name, path)
        try:
            with open(path, encoding="utf-8") as f:
                # 如果数据是列表类型，则解包后再进行替换
                if isinstance(data, list):
                    template = Template(f.read()).substitute(*data)
                # 否则直接替换
                else:
                    # data = template_preposition.exaPlanPreposition(data)
                    template = Template(f.read()).substitute(data)
            logger('template').info("模板替换成功，替换的模板为{}".format(path))
            # 将替换的内容转换至字典格式并返回
            return yaml.safe_load(template)
        except Exception as e:
            logger('template').info(e, exc_info=True)


handle_template = Handle_templata()


if __name__ == '__main__':
    # save_place_template = yaml_handle.get_yaml("savePlaceTestCase.yml")["savePlace"]["data"]
    # print(save_place_template)
    save_place = {'planCode': '2fb681c043d546db878ea1e6461ca8d2', 'planCoding': '530100202205170006', 'studentCode': '6087d9952c194c129fb9530b938bd361', 'examSiteCode': 'fcd79f2dc2f54ad0a04c166a27e9e308', 'siteType': 0, 'startTime': '2022-05-17 20:29:08', 'endTime': '2022-05-17 20:29:09', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXJyZW50IjoxNjUyNzkwNzkwNDQ1LCJleHAiOjE2NTI3OTQzOTAsImlhdCI6MTY1Mjc5MDc5MCwidXNlckNvZGUiOiJiYTRkNzgxZTUyM2M0MzczOGI4ZDZiNGU1ZmEwY2QyMCJ9.rl4zBrIiQQKNzMCom0yPNEKKuwedybNuiFtgaq1FPXU'}
    print(handle_template.template(save_place, 'savePlaceApi.yml'))
    # data["token"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXJyZW50IjoxNjUyNjA1Mzk3MDA3LCJleHAiOjE2NTI2MDg5OTcsImlhdCI6MTY1MjYwNTM5NywidXNlckNvZGUiOiJhYmZjMDg4ZTM5MjU0YzA4YTZlMzY1MDkxODg1YWFiMCJ9.njWTowOGnhm4ohPeZIAbXOkRnbrYHHN3YutsEY1xon0"
    # print(data)
    # # data=handle_template.template(data, "saveExaPlanApi.yml")
    # # print(data)
    # from base.base_requests import base_requests
    # res = base_requests.parametric_requests(data, "saveExaPlanApi.yml")
    # # print(res)