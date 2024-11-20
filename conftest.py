"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/3/14 0014 下午 4:50
@Auth ： 最下级测试工程师
@File ：conftest.py
@IDE ：PyCharm
"""
from typing import List
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')