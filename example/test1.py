#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/5 9:24
# software: PyCharm
age=[23,45,123,55]
print "count " ,age.count(23)
age.append(56)
print age
#移除某项
age_pop=age.pop(1)
print "删除的项",age_pop
print "列表现在为：",age
#反向列表
name=['jack','ma','wangkai']
name.reverse()
print "翻转以后的显示：", name
# 降序
#获取列表的第二个元素
def takeSecomd(elem):
    return elem[1]
# 列表
random=[(2,2),(3,4),(4,1),(1,3)]
#制定第二个元素排序
random.sort(reverse=True)
# 输出类别
print '排序列表：',random

