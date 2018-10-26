#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/10/26 17:33
# software: PyCharm
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('C:\\Users\\houjinkai\\PycharmProjects\\untitled\\selenium\\test1.html')

# 1.xpath: `.`代表当前节点; '..'代表父节点
print driver.find_element_by_xpath("//div[@id='C']/../..").text

# 2.xpath轴 parent
print driver.find_element_by_xpath("//div[@id='C']/parent::*/parent::div").text

driver.quit()
