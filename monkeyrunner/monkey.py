#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/10 14:49
# software: PyCharm
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device=MonkeyRunner.waitForConnection()

#启动activity（这里启动qq）

device.startActivity(component="com.tencent.mobileqq/.activity.SplashActivity")

#登录界面，点击账号输入框

device.touch(60,300,'DOWN_AND_UP')

#输入qq账号

device.type('3469191693')