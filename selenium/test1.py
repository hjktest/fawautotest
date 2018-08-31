#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/8/21 13:06
# software: PyCharm
class DemoClass2:
    @classmethod
    def classPrint(self):
        print("class method")
    def objPrint(self):
        print("obj method")

class DemoClass3:
    @staticmethod
    #不需要传入参数
    def classPrint():
        print("class method")
    def objPrint(self):
        print("obj method")
class DemoClass1:
    def classPrint(self):
        print("class method")
    def objPrint(self):
        print("obj method")
# DemoClass2.classPrint()
# obj=DemoClass2()
# obj.classPrint()
# DemoClass3.classPrint()
obj=DemoClass1()
#通过类调用函数
DemoClass1.classPrint(obj)
#通过实例调用函数
obj.classPrint()
obj.objPrint()