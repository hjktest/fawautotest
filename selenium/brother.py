#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: brother.py
@time: 2018/11/4 17:29
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('C:\\Users\\hjk\\PycharmProjects\\fawautotest\\selenium\\test3.html')

# 1.xpath,通过父节点获取其哥哥节点
print driver.find_element_by_xpath("//div[@id='D']/../div[1]").text

# 2.xpath轴 preceding-sibling
print driver.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text

driver.quit()
