# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re
import HTMLTestRunner

#一汽大众电商
class Faw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_faw(self):
        driver = self.driver
        driver.get("https://mall.faw-vw.com/views/index.html")
        # u"""定制车"""
        driver.find_element_by_link_text(u"定制车").click()
        # u"""新车"""
        driver.find_element_by_link_text(u"买新车").click()
        driver.find_element_by_link_text(u"二手车").click()
        driver.find_element_by_link_text(u"优选车品").click()
        driver.find_element_by_link_text(u"经销商").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='全部'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='经销商'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='经销商'])[1]/following::input[1]").clear()
        searchkey=["CC",U"捷达"];
        for key in searchkey:
             print key
             driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='经销商'])[1]/following::input[1]").send_keys(key)
             driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='经销商'])[1]/following::div[2]").click()
             driver.find_element_by_xpath(
                 u"(.//*[normalize-space(text()) and normalize-space(.)='经销商'])[1]/following::input[1]").clear()
    def test_login(self):
        # u"""登录"""
        driver = self.driver
        driver.get("https://mall.faw-vw.com/views/index.html")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='快捷登录'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='快捷登录'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='快捷登录'])[1]/following::input[1]").send_keys(
            "13601374209")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='快捷登录'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='快捷登录'])[1]/following::input[2]").send_keys(
            "test123")
        url=driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='快捷登录'])[1]/following::input[3]").click()
        # print driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::span[1].").text()
        a=driver.find_element_by_class_name("fnList").text
        print a
        self.assertIn(u"我的订单",a,msg="登录失败")




    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
    # testunit=unittest.TestSuite()
    # testunit.addTest(Faw.test_faw())
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # # 定义个报告存放路径，支持相对路径
    # filename = "C:\\selenium\\report\\" + now + '_result.html'
    # fp = file(filename,"wb")
    # # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'测试报告',
    #     description=u'用例执行情况'
    # )
    # runner.run(testunit)
    # runner.close()
