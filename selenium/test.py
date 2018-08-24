#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/8/23 17:47
# software: PyCharm
import unittest
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4+5, 9)

    def test2(self):
        self.assertNotEqual(5*2, 11)

    def test3(self):
        self.assertTrue(4+5==9, "The result is True")

    def test4(self):
        self.assertTrue(4+5==9, "assertion fails")

    def test5(self):
        self.assertIn(3,[1,2,3])

    def test6(self):
        self.assertNotIn(11,range(5))

if __name__=="__main__":
    unittest.main()