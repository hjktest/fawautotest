#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/26 11:06
# software: PyCharm
import time
from selenium import webdriver
import urllib
from wx import Image
import pandas as pd

def gethtml(url):
    loginurl='https://www.douban.com/'    # 登录页面

    browser = webdriver.PhantomJS()s
    browser.get(loginurl)    # 请求登录页面
    browser.find_element_by_name('form_email').clear()  # 获取用户名输入框，并先清空
    browser.find_element_by_name('form_email').send_keys(u'648073731@qq.com') # 输入用户名
    browser.find_element_by_name('form_password').clear()  # 获取密码框，并清空
    browser.find_element_by_name('form_password').send_keys(u'hjk12345') # 输入密码

    # 验证码手动处理,输入后，需要将图片关闭才能继续执行下一步
    captcha_link = browser.find_element_by_id('captcha_image').get_attribute('src')
    urllib.request.urlretrieve(captcha_link,'captcha.jpg')
    Image.open('captcha.jpg').show()
    captcha_code = input('Pls input captcha code:')
    browser.find_element_by_id('captcha_field').send_keys(captcha_code)

    browser.find_element_by_css_selector('input[class="bn-submit"]').click()
    browser.get(url)
    browser.implicitly_wait(10)
    return(browser)
def getComment(url):
     i = 1
     AllArticle = pd.DataFrame()
     browser = gethtml(url)
     while True:
        s = browser.find_elements_by_class_name('comment-item')
        from statsmodels.compat import pandas
        articles = pd.DataFrame(s,columns = ['web'])
        articles['uesr'] = articles.web.apply(lambda x:x.find_element_by_tag_name('a').get_attribute('title'))
        articles['comment'] = articles.web.apply(lambda x:x.find_element_by_class_name('short').text)
        articles['star'] = articles.web.apply(lambda x:x.find_element_by_xpath("//*[@id='comments']/div[1]/div[2]/h3/span[2]/span[2]").get_attribute('title'))
        articles['date'] = articles.web.apply(lambda x:x.find_element_by_class_name('comment-time').get_attribute('title'))
        articles['vote'] = articles.web.apply(lambda x:np.int(x.find_element_by_class_name('votes').text))
        del articles['web']
        AllArticle = pd.concat([AllArticle,articles],axis = 0)
        print ('第' + str(i) + '页完成!')

        try:
            if i==1:
                browser.find_element_by_xpath("//*[@id='paginator']/a").click()
            else:
                browser.find_element_by_xpath("//*[@id='paginator']/a[3]").click()
            browser.implicitly_wait(10)
            time.sleep(3) # 暂停3秒
            i = i + 1
        except:
            AllArticle = AllArticle.reset_index(drop = True)
           return AllArticle
     AllArticle = AllArticle.reset_index(drop = True)
     return AllArticle
if __name__ == "__main__":
    unittest.main()