#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/11/6 13:47
# software: PyCharm
def selectedSort(mylist):
    #获取list的长度
    length=len(mylist)
    #一共进行多少次比较
    for i in range(0,length-1):
        # 默认设置最小值得index为当前值
        smallest=i
        # 用当先最小index的值分别与后面的值进行比较,以便获取最小index
        for j in range(i+1,length):
            if mylist[j]<mylist[smallest]:
                # tmp=mylist[j]
                # mylist[j]=mylist[smallest]
                # mylist[smallest]=tmp
                mylist[j],mylist[smallest]=mylist[smallest],mylist[j]
        #打印每一轮比较好的列表
        print("Round ",i,":",mylist)


mylist=[9,4,5,8,3]
print("Selected Sort: ")
selectedSort(mylist)