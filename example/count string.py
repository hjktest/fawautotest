#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/4 14:15
# software: PyCharm
a = "hello world"
aDic = {}
for i in a:
    if i in aDic:
        aDic[i] += 1
        print "if"
        print i,aDic[i]
    else:
        aDic[i] = 1
        print "else"
        print i,aDic[i]
print(aDic)




