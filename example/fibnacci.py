#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/6 11:26
# software: PyCharm
def fibnacci():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b

fib=fibnacci()
# for i in range(10):
#     print fib.next()

print [fib.next() for i in range(10)]
