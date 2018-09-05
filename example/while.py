#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/5 13:58
# software: PyCharm
numbers=[12,3,5,22,123,44,7]
even=[]
odd=[]
while len(numbers)>0:
    number=numbers.pop()
    if(number % 2 ==0):
        even.append(number)
        print "偶数"
        print even
    else:
        odd.append(number)
        print "奇数"
        print odd

