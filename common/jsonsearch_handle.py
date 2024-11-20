"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/3/18 0018 下午 3:17
@Auth ： 最下级测试工程师
@File ：jsonsearch_handle.py
@IDE ：PyCharm
"""
from jsonsearch import JsonSearch

data = {
    "returnCode": 200,
    "success": True,
    "data": {
        "orgCode": "a9af206d613748489ca665ae4d118850",
        "filInfoCode": None,
        "orgName": "临沧市技能鉴定报名机构",
        "socialCreditCode": "CA87TDLSQ13ZX",
        "unitAddress": "浙江温州江南皮革厂",
        "contractPerson": "黄鹤",
        "contractPhone": "17896547785",
        "isFil": 1,
        "skillLevelIdentification": 8,
        "professionalQualification": -1,
        "specialAbility": 8,
        "officialExamination": 8
    },
    "returnMsg": "操作成功!",
    "planCode": None,
    "planCodes": None,
    "content": None,
    "logIgnored": False
}


def json_search(res, key):
    jsondata = JsonSearch(object=res, mode='j')
    return jsondata.search_first_value(key)

if __name__ == '__main__':
    print(jsonsearch_handle(data, "returnCode"))


