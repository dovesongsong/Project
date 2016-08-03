#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filename: handle_mariadb.py

"""
Function:
连接及操作mariadb数据库

Author:     Hermes
Version:    2016-06-18
Contact:
"""

import pymysql

#连接配置信息
# config = {
#           'host':'10.224.192.110',
#           'port':3306,
#           'user':'user1',
#           'passwd':'deppon',
#           'db':'online_ordering',
#           'charset':'utf8',
#           }

def connMariadb():
    conn = pymysql.connect(user='user1', passwd='deppon',host='10.224.192.110', db='online_ordering',charset='utf8')
    cur = conn.cursor()
    return cur

def selectMariadb(a,sql):
    a.execute(sql)
    return a

def insertMariadb(a,sql):
    a.execute(sql)
    return a

def updateMariadb(a,sql):
    a.execute(sql)
    return a

def deleteMariadb(a,sql):
    a.execute(sql)
    return a

if  __name__ == "__main__":
    try:
        # 创建连接
        a = connMariadb()
        selectSql = "select * from test"
        insertSql = "insert into test(id,name) values (4, 'Zhyea')"
        updateSql = "update test set name = 'xxx' where id = 2"
        deleteSql = "delete from test where id = 3"
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        # 打印语句
        print(selectSql)
        print(insertSql)
        print(updateSql)
        print(deleteSql)
        # insertMariadb(a,insertSql)
        deleteMariadb(a,deleteSql)
        a.connection.commit()
        selectMariadb(a,selectSql)
        for row in a.fetchall():
            print('%s\t%s' %row)
        # 执行sql语句，更新记录
    finally:
        a.close();
