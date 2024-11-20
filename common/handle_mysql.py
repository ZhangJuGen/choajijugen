"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@Time ： 2022/1/13 0013 下午 4:27
@Auth ： 最下级测试工程师
@File ：handle_mysql.py
@IDE ：PyCharm
"""

import pymysql
from conf import config

'''
pip install PyMySQL==0.9.3
'''


class DbConnect():

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
    '''查询数据库'''
    db = DbConnect()
    result = db.select(select_sql)  # 查询
    db.close()
    return result


def execute_sql(insert_sql):
    '''执行sql'''
    db = DbConnect()
    db.execute(insert_sql)  # 查询
    db.close()


if __name__ == '__main__':
    print(config.HOST,config.USER,config.PASSWORD,config.PORT,config.database)
    role_id = select_sql("SELECT * from exa_plan")
    print(role_id)
