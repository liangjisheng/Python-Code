# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = decorate_4
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 11:29
"""
import time
# 装饰器本身也可以带参数


def deco(arg=True):
    if arg:
        def _deco(func):
            def wrapper(*args, **kwargs):
                startTime = time.time()
                func(*args, **kwargs)
                endTime = time.time()
                msecs = (endTime - startTime) * 1000
                print('time is %f ms' % msecs)
            return wrapper
    else:
        def _deco(func):
            return func
    return _deco


@deco(False)
def myFunc():
    print('start myFunc')
    time.sleep(0.6)
    print('end myFunc')


@deco(True)
def addFunc(a, b):
    print('start addFunc')
    time.sleep(0.6)
    print('result is %d' % (a + b))
    print('end addFunc')


print('myFunc is', myFunc.__name__)
# 如果装饰器本身需要支持参数，那么装饰器就需要多一层的内嵌函数
# myFunc() = deco(False)(myFunc()), deco(False)返回else分支的装饰器，禁用计时功能
myFunc()
print()
print('addFunc is', addFunc.__name__)
# addFunc(3, 4) = deco(True)(addFunc(3, 4)), deco(True)返回if分支的装饰器,启用计时功能
addFunc(3, 4)
