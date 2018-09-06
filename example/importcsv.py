#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/6 15:54
# software: PyCharm
from pandas.io.parsers import read_csv
df=read_csv("D:\lingjian.csv")
# print "DataFramer: ", df
print "Shape:",df.shape #大小
print "Length:",len(df)  #长度

print "Column Headers",df.columns #得到每列的标题
print "Data type",df.dtypes   #得到每列数据的类型
print "Index:",df.index #索引
