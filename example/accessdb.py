#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/6 17:31
# software: PyCharm
import statsmodels.api as sm
from pandas.io.sql import read_sql
import sqlite3
with sqlite3.connect(":memory:") as con:
    c = con.cursor()
    data_loader = sm.datasets.sunspots.load_pandas()  # 加载数据
    df = data_loader.data
    rows = [tuple(x) for x in df.values]
    con.execute("CREATE TABLE SUNSPOTS(year,sunactivity)")
    con.executemany("INSERT INTO sunspots(year,sunactivity) VALUES(?,?)", rows)  # 执行多次SQL语句
    c.execute("SELECT COUNT(*) FROM sunspots")  # 统计数据表中元组数
    print c.fetchone()
    print "Deleted", con.execute("DELETE FROM sunspots where sunactivity>20").rowcount, "rows"  # rowcount表示受影响的行
    print read_sql("SELECT * FROM sunspots where year<1732",
                   con)  # 如果把数据库连接到pandas，使用read_sql函数执行查询就可以返回pandas DataFrame了
    con.execute("DROP TABLE sunspots")
c.close()
