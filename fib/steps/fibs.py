#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:houjinkai
# datetime:2018/9/7 14:46
# software: PyCharm
from behave import *
from hamcrest import *


def fibs(num):
    a = b = 1
    for i in range(num):
        yield a
        a, b = b, a + b


@given('we have the number {number}')
def have_number(context, number):
    context.fib_number = int(number)


@when('we calc the fib')
def calc_fib(context):
    context.fib_number = list(fibs(context.fib_number))[-1]


@then('we get the fib number {number}www.8555388.cn/')
def get_number(context, number):
    context.expected_number = int(number)
    assert_that(context.fib_number, equal_to(context.expected_number), "Calc fib number: %d" % context.fib_number)