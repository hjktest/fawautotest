#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: brother 2.py
@time: 2018/11/4 17:31
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('C:\\Users\\hjk\\PycharmProjects\\fawautotest\\selenium\\test3.html')

# 1.xpath，通过父节点获取其弟弟节点
print driver.find_element_by_xpath("//div[@id='D']/../div[3]").text

# 2.xpath轴 following-sibling
print driver.find_element_by_xpath("//div[@id='D']/following-sibling::div[1]").text

# 3.xpath轴 following
print driver.find_element_by_xpath("//div[@id='D']/following::*").text

# 4.css selector +
print driver.find_element_by_css_selector('div#D + div').text

# 5.css selector ~
print driver.find_element_by_css_selector('div#D ~ div').text

driver.quit()
