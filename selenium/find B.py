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
print driver.find_element_by_xpath("//div[@id='B']/div").text
# 3.css selector父子关系寻找
print driver.find_element_by_css_selector('div#B>div').text

# 4.css selector nth-child
print driver.find_element_by_css_selector('div#B div:nth-child(1)').text

# 5.css selector nth-of-type
print driver.find_element_by_css_selector('div#B div:nth-of-type(1)').text

# 6.xpath轴 child
print driver.find_element_by_xpath("//div[@id='B']/child::div").text

driver.quit()
