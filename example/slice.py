#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/7 16:02
# software: PyCharm
l=['Adam','Lisa','Bart','Paul']
print l[:3] #取前三个元素
print l[1:3] # 取第2到3的元素
print l[:] #取全部元素，相当于复制一遍
# 第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个
print l[::2]
print l[:-2]#截止到索引为-2
print l[-2:]#
print l[-3:-1]
print l[-4:-1:2]
ran=range(1,101)
print ran[0:10]#取前10个数
print ran[2::3]#取3的倍数
print ran[4:51:5]#不大于50的5的倍数。
#倒叙排列
str="l low python!"
print str[::-1]

#请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
def firstCharUpper(s):
    s[0:1].upper()
    s1=s[0:1].upper()+s[1:]
    return s1

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
