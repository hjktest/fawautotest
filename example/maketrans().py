#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/4 13:40
# software: PyCharm
from string import maketrans   # 必须调用 maketrans 函数。以下实例展示了使用maketrans() 方法将所有元音字母转换为指定的数字

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab);