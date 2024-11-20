# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:mysql_handelr.py
@time:2024/11/12
"""
import pymysql
from conf import config


class DbConnect:

    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(database=config.database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  host=config.HOST,
                                  user=config.USER,
                                  passwd=config.PASSWORD,
                                  port=config.PORT)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


def select_sql(select_sql):
    # 查询数据库
    db = DbConnect()
    result = db.select(select_sql)  # 查询
    db.close()
    return result


def execute_sql(insert_sql):
    # 执行sql
    db = DbConnect()
    db.execute(insert_sql)  # 修改
    db.close()


if __name__ == '__main__':
    sql = execute_sql("insert into sys_message(phone,verifyCode,create_time,device_type,use_status'') "
                                    "VALUES('{}','{}','{}','{}','{}')".format(config.PHONE, config.VERIFYCODE, '2024-11-18 14:59:01',
                                                                              'DIC_DEVICE_TYPE_1', '0'))
    print(sql)
    # execute_sql("insert into sys_message(phone,verifyCode,create_time,device_type,use_status) VALUES('18229790602',"
    #             "'666666','2024-11-18 10:55:18','DIC_DEVICE_TYPE_1',0)")
    # role_id = select_sql("SELECT * from sys_message order by create_time desc limit 10")
    # print(role_id)
