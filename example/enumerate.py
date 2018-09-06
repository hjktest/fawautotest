#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/6 10:50
# software: PyCharm
i=0
seq=["one","two","three"]
for element in seq:
    seq[i]='%d: %s ' % (i,seq[i])
    i+=1

print seq

seq=["one","two","three"]
for i,element in enumerate(seq):
    seq[i]='%d : %s' %(i,seq[i])

print seq