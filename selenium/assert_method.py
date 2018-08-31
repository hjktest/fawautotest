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
    # 判断a与1.b是否一致，msg类似备注，可以为空
    def test1(self):
        self.assertEqual(4+5, 9)

    # 判断a与b是否不一致
    def test2(self):
        self.assertNotEqual(5*2, 11)

    # 判断a是否为True
    def test3(self):
        self.assertTrue(4+5==9, "The result is True")

    # 判断a是否为False
    def test4(self):
        self.assertFalse(4+5==8, "assertion fails")

    def test5(self):
        self.assertIn(3,[1,2,3],msg='不包含')

    def test6(self):
        self.assertNotIn(11,range(5))
    def test7(self):
        self.assertGreater(7,6,msg="真的大于")

    # 判断a与b的对象是否相同，成立则True，否则False
    def test8(self):
        self.assertIs(1,1,"内容不一致")
    def test9(self):
        self.assertIsNot(1,2,"内容一致")

    # 注：places与delta不能同时存在，否则出异常

    # 若a==b，则直接输入正确，不判断下面的过程

    # 若delta有数，places为空，判断a与b的差的绝对值是否<=delta，满足则正确，否则错误

    # 若delta为空，places有数，判断b与a的差的绝对值,取小数places位，等于0则正确，否则错误

    # 若delta为空，places为空，默认赋值places=7判断
    def test10(self):
        self.assertAlmostEqual(5,4,places=1)
        self.assertAlmostEqual(5, 2, delta=4)
        self.assertAlmostEqual(5, 2, delta=2)
        self.assertAlmostEqual(2, 2.005, places=1)
        self.assertAlmostEqual(2, 2.05, places=3)
        #self.assertNotAlmostEqual(a, b, delta=c)#a不等于b 同时 a-b>c 则正确，否则错误
        self.assertNotAlmostEqual(2,2,places=2)
        # self.assertDictEqual(a, b)  # 判断字典a和字典b是否相等，a,b为字典

        # 注：sorted排序，方法内部为，将a, b分别list，生成各自列表，在sorted排序在比对
        #
        # self.assertMultiLineEqual(a, b)  # 比较a文本与b文本是否一致，即便多了个换行，也会区分
        #
        # self.assertLess(a, b)  # 判断a<b 成立则通过，否则失败
        #
        # self.assertLessEqual  # 判断a<=b 成立则通过，否则失败
        #
        # self.assertGreater  # 判断a>b 成立则通过，否则失败
        #
        # self.assertGreaterEqual  # 判断a>=b 成立则通过，否则失败
        #
        # self.assertIsNone(obj=””)  # 判断obj=None 成立则通过，否则失败
        #
        # self.assertIsNotNone  # 判断obj=None 成立则失败，否则通过
        #
        # self.assertIsInstance(a, b)  # 判断a的数据类型是否为b，isinstance(a,b) 成立则通过，否则失败
        #
        # self.assertNotIsInstance  # 判断同上相反
        #
        # self.assertRaisesRegexp  # 正则判断匹配，没仔细看，过程复杂
        #
        # self.assertRegexpMatches(a, b)  # 正则匹配 同re.search(b,a)匹配有则成功，否则失败
        #
        # 注：a为匹配的正则表达式，必须字符型，b
        # 为要匹配的内容
        #
        # self.assertNotRegexpMatches  # 同上，判断相反




if __name__=="__main__":
    unittest.main()