#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/5 11:40
# software: PyCharm
# 加了星号（*）的变量名会存放所有未命名的变量参数。不定长参数实例如下：
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;

# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用printme函数
printme("My string");
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );
printinfo("asdf",23,'23')