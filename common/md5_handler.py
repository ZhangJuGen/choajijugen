"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/5/13 0013 下午 4:47
@Auth ： 最下级测试工程师
@File ：md5_handler.py
@IDE ：PyCharm
"""

import hashlib

md5 = hashlib.md5()     # 应用MD5算法

data = input("请输入加密内容：")

md5.update(data.encode('utf-8'))

print(md5.hexdigest())