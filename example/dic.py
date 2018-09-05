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
seq=('google','Runoob','Taobao')
dict=dict.fromkeys(seq)
print "新字典:%s" % str(dict)
dict=dict.fromkeys(seq,10)
print "新字典:%s" % str(dict)
#遍历字典元素
dict={'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print "字典值：%s" % dict.items()
#遍历字典列表
for key,values in dict.items():
    print key,values
# 返回key,values值
dict = {'Name': 'Zara', 'Age': 7}
print "key : %s" % dict.keys()
print "values: %s" % dict.values()
#Python 字典 pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print pop_obj
print site
#popitem Python 字典 popitem() 方法随机返回并删除字典中的一对键和值。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)