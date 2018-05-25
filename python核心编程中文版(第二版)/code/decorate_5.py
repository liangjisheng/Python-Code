# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = decorate_5
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 11:43
"""
import time


def deco_1(func):
    print('enter into deco_1')

    def wrapper(a, b):
        print('enter into deco_1_wrapper')
        func(a, b)
    return wrapper


def deco_2(func):
    print('enter into deco_2')

    def wrapper(a, b):
        print('enter into deco_2_wrapper')
        func(a, b)

    return wrapper


@deco_1
@deco_2
def addFunc(a, b):
    print('result is %d' % (a + b))


# addFunc(3, 4) = deco_1(deco_2(addFunc(3, 4)))
addFunc(3, 4)
