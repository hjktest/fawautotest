#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/8/31 14:49
# software: PyCharm
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n
if __name__ == "__main__":
    print fact(5)