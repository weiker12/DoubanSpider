#!/usr/bin/env python
# coding: utf-8
import MySQLdb
from threading import Lock

db_lock = Lock()

# 数据库连接基类
class SqlDB:
    # 初始化
    def __init__(self, host, user, passwd, database, charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        try:
            self.db = MySQLdb.connect(host=self.host,
                                      user=self.user,
                                      passwd=self.passwd,
                                      db=self.database,
                                      port=3306,
                                      charset=self.charset,
                                      use_unicode=True)
            self.cursor = self.db.cursor()
            # 基本设置
            self.cursor.execute('SET NAMES utf8;')
            self.cursor.execute('SET CHARACTER SET utf8;')
            self.cursor.execute('SET character_set_connection=utf8;')
            self.db.commit()
            self.cursor.execute("SELECT VERSION()")
            ver = self.cursor.fetchone()
        except Exception, e:
            print e
            raise e

    # 执行
    def execute(self, sql):
        try:
            db_lock.acquire()
            self.cursor.execute(sql)
            self.db.commit()
            db_lock.release()
        except Exception as err:
            self.db.commit()
            db_lock.release()
            raise err

    # 单个插入
    def insert(self, sql, data_list):
        try:
            db_lock.acquire()
            self.cursor.execute(sql, data_list)
            self.db.commit()
            db_lock.release()
        except Exception as err:
            self.db.commit()
            db_lock.release()
            raise err

    # 批量插入
    def batch_insert(self, sql, data_list_list):
        try:
            db_lock.acquire()
            self.cursor.execute(sql, data_list_list)
            self.db.commit()

            db_lock.release()
        except Exception as err:
            self.db.commit()
            db_lock.release()
            raise err

    # 查询
    def select(self, sql):
        try:
            db_lock.acquire()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.db.commit()
            db_lock.release()
            return result
        except Exception as err:
            self.db.commit()
            db_lock.release()
            raise err
    # 插入
    def insert(self, tablename, column_list, value_list):
        column_str = ''
        if (len(column_list) > 0):
            column_str = ','.join(column_list)
            column_str = '(' + column_str + ')'
        s_holder = []

        try:
            length = len(value_list)
            for i in range(length):
                s_holder.append('%s')
            placeholder = ','.join(s_holder)
            sql = "insert into {0} {1} values ({2})".format(tablename, column_str, placeholder)
            self.batch_insert(sql, value_list)
        except Exception, e:
            print e

    def select_column(self, sql):
        result = self.select(sql)
        return [row[0] for row in result]

    def select_row(self, sql):
        result = self.select(sql)
        return result[0]

    def select_scalar(self, sql):
        row = self.select_row(sql)
        return row[0]

    def get_table_id(self, sql):
        cur = self.db.cursor()
        cur.execute(sql)
        row = cur.fetchall()
        return row[len(row) - 1]
