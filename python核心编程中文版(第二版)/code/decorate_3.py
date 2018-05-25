# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = decorate_3
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 10:33
"""
import time
# deco函数就是最原始的装饰器，他的参数是一个函数，返回值也是一个函数


def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('time is %d ms' % msecs)
    return wrapper


@deco
def func():
    print('hello')
    time.sleep(1)
    print('world')


def deco1(func):
    def wrapper(a, b):
        startTime = time.time()
        func(a, b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('time is %d ms' % msecs)
    return wrapper


@deco1
def func1(a, b):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is %d' % (a + b))


def deco2(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('time is %d ms' % msecs)

    return wrapper


@deco2
def func2_1(a, b):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is %d' % (a + b))


@deco2
def func2_2(a, b, c):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is %d' % (a + b + c))


def deco3_1(func):
    def wrapper(*args, **kwargs):
        print('this is deco3_1')
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('time is %d ms' % msecs)
        print('deco3_1 end here')
    return wrapper


def deco3_2(func):
    def wrapper(*args, **kwargs):
        print('this is deco3_2')
        func(*args, **kwargs)
        print('deco3_2 end here')
    return wrapper


@deco3_1
@deco3_2
def func3(a, b):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is %d' % (a + b))


if __name__ == '__main__':
    # 没有参数的装饰器
    # f = func
    # f()

    # 带有参数的装饰器
    # f1 = func1
    # f1(3, 4)

    # 带有不定参数的装饰器
    # func2_1(3, 4)
    # func2_2(3, 4, 5)

    # 多个装饰器
    # 先用deco3_2装饰func3得到一个函数对象，在用deco3_1装饰前面得到的函数对象
    # 得到最终的可调用函数对象
    func3(3, 4)
