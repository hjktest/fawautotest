#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/8/31 15:02
# software: PyCharm
from itertools import combinations
# for x in range(1,101):
#     print "three"[x%3*len('three')::]+"five"[x%5*len("five")::] or x
nfc=["packers","49ers"]
afc=["Ravens","Patriots"]
for teama,teamb in zip(nfc,afc):
    print teama + " vs." +teamb
# 带索引的列表迭代
teams=["Packers", "49ers", "Ravens", "Patriots"]
for index,team in enumerate(teams):
    print index,team
#查找所有的组合
teams=["bananas","orange","pair","apple","greentea"]
for fruit in combinations(teams,3):
    print fruit