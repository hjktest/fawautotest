#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/10/26 17:11
# software: PyCharm
# https://blog.csdn.net/huilan_same/article/details/52541680
from selenium import  webdriver
driver=webdriver.Chrome()
driver.get('C:\\Users\\houjinkai\\PycharmProjects\\untitled\\selenium\\test.html')
#1串联寻找
print driver.find_element_by_id('B').find_element_by_tag_name('div').text
# 2.xpath父子关系寻找