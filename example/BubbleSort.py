#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/11/6 15:49
# software: PyCharm
def bubblesort(nums):
    for i in range (len(nums)-1): # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):# ｊ为列表下标
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        print("Round ", i, ":", nums)

    return nums

nums=[2,5,1,6,3,9]
print bubblesort(nums)
