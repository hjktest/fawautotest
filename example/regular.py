#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/5 15:09
# software: PyCharm
import re
print(re.match('www','www.runnoob.com').span())
print(re.match('com','www.runnoob.com'))
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

# 身份证 1102231990xxxxxxxx
import re
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{3})',s)
print(res.groupdict())