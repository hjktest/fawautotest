#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/4 11:40
# software: PyCharm
str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.find(str2)
print str1.find(str2,10)
print str1.find(str2,40)

str = u"this2009";
print str.isnumeric();

str = u"23443434";
print str.isnumeric();
# 大写字母小写
str = "THIS IS STRING EXAMPLE....WOW!!!";

print str.lower();
# 小写字母大写
str = "this is string example....wow!!!";
print str.upper()
#join 用法
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
#lstrip 截掉左边的空格
str = "     this is string example....wow!!!     ";
print str.lstrip();
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8');
#rstrip删除右侧的空格
str = "     this is string example....wow!!!     ";
print str.rstrip();
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8');
#返回分割的字符串

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ', 1 );