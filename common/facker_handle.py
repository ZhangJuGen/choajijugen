"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/5/13 0013 下午 5:39
@Auth ： 最下级测试工程师
@File ：facker_handle.py
@IDE ：PyCharm
"""
import json
import random
from datetime import datetime, timedelta

from faker import Faker
from common.wrappar import get_time


class RandomFaker:
    """
    Faker库的调用
    name()	生成姓名
    phone_number()	生成11位手机号
    email()	生成电子邮件
    address()	生成地址
    ssn(min_age=18,max_age=100)	生成身份证号(最小年龄，最大年龄)
    text(max_nb_chars=100)	生成一段100字符的假文
    user_agent()	生成一个随机user_agent头
    """

    def __init__(self):
        self.f = Faker("zh-CN")

    @get_time
    def random_name(self):
        return self.f.name()

    def random_phone(self):
        return self.f.phone_number()

    def random_email(self):
        return self.f.email()

    def random_address(self):
        return self.f.address()

    def random_id(self):
        return self.f.ssn()

    def random_text(self):
        return self.f.text(max_nb_chars=10)

    @get_time
    def exaPlanName(self):
        nameList = ['翠花', '狗蛋', '铁柱', '狗剩', '草根', '铁锤', '大力', '腿子', '甘萌', '鞠花', '你就是歌姬吧', \
                    '你就是歌王吧', '史珍湘', '大沙雕', '腿毛', '狗子', 'lick dog no house', '9527']
        return random.choice(nameList)

    @get_time
    def filName(self):
        return '备案'

    @get_time
    def random_current_time(self):
        return ''

    @staticmethod
    def current_time():
        time = datetime.now().strftime("%Y-%m-%d 00:00:00")
        return str(time)

    @staticmethod
    def after_time():
        afterTime = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d 23:59:59")
        return str(afterTime)


random_faker = RandomFaker()

if __name__ == '__main__':
    random_faker = RandomFaker()
    print("""
        姓名：{}
        身份证：{}
        电话号码：{}
        邮箱：{}
        随机一段文字: {}
        当期时间: {}
        十天后: {}
        {}
            """.format(
        random_faker.exaPlanName(),
        random_faker.random_id(),
        random_faker.random_address(),
        random_faker.random_phone(),
        random_faker.random_text(),
        random_faker.current_time(),
        random_faker.after_time(),
        random_faker.random_current_time()
    ))
