#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/5 10:03
# software: PyCharm
dict={'name':'Zara','Age':23}
print "Start Len: %d " % len(dict)
dict.clear()
print "End len: %d" % len(dict)
#浅复制
dict1={'name':'Zara','Age':23}
dict2=dict1.copy()
print "New Dictinary: %s" % dict2
print "New Dictinary: %s" % str(dict2)
#直接赋值和 copy 的区别
dict1={'user':'runoob','num':[1,2,3]}
dict2=dict1# 浅拷贝: 引用对象
dict3=dict1.copy()# 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
#修改data数据
dict1['user']='root'
dict1['num'].remove(3)
#输出结果
print dict1
print dict2
print dict3
#Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
