#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/5 15:09
# software: PyCharm
import re
print(re.match('www','www.runnoob.com').span())
print(re.match('com','www.runnoob.com'))
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 解析:
#
# 首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
#
#  (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
#  (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
#  后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
# matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
#
# matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
#
# matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的
#
# 因为只有匹配结果中只有两组，所以如果填 3 时会报错。
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