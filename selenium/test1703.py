#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/8/27 17:03
# software: PyCharm
list=[10,2,34,123,434,1,66,89]
print "原始数据"
print list
def bubble_sort(list):
    count=len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if list[i]>list[j]:
                # tmp=list[i]
                # list[i]=list[j]
                # list[j]=tmp
                list[i],list[j]=list[j],list[i]
        print "第 %d 次" % (i)
        print list

    return list
print "冒泡最终的的结果"
print bubble_sort(list)
