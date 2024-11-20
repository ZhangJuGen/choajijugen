# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/7 16:35
@Auth ： Zhang
@File ：random_faker.py
@IDE ：PyCharm
"""
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





if __name__ == '__main__':
    random_faker = RandomFaker()
    print("""
        姓名：{}
        身份证：{}
        电话号码：{}
        邮箱：{}
            """.format(
        random_faker.random_name(),
        random_faker.random_id(),
        random_faker.random_address(),
        random_faker.random_phone()))
