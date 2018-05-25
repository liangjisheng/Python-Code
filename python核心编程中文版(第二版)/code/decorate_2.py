# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = decorate_2
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 10:04
"""
# 有参数的装饰器


import time
import datetime


def outter(func):
    def inner(args):
        start = datetime.datetime.now()
        func(args)
        end = datetime.datetime.now()
        cost = end - start

        print("execute %s spend %s" % (func.__name__, cost.total_seconds()))
    return inner


# 返回当前的时间截，python中的time模块里面大部分实现和c语言中的time.h头文件中的函数一样
# 函数所代表的意思也是一样的
print(time.time())
print(time.localtime())
print(time.gmtime())
print(time.asctime())
