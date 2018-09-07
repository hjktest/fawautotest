#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/6 17:08
# software: PyCharm
import sqlite3
with sqlite3.connect(":memory:")as con:
        c=con.cursor()#创建数据库
        c.execute('''CREATE TABLE sensors(data text,city text,code text,sensor_id real,temperature real)''') #新建表，text和real分别表示字符串和数值的类型
        for table in c.execute("select name from sqlite_master where type='table'"):
            print "Table",table[0]
            c.execute("INSERT INTO sensors VALUES('2016-11-05','Utrecht','Red',42,15.14)")
            c.execute("select * from sensors")
            print c.fetchone()#输出插入记录
            con.execute("drop table sensors")
            print "# of tables", c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
c.close()
