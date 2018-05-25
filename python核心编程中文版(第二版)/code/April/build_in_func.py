# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = build_in_func
@author = Liangjisheng
@create_time = 2018/4/5 0005 上午 10:14
"""

print(type(sum))
print(dir(sum))
print(type(dir))


def foo(): pass


print(type(foo))
lambdaFunc = lambda x: x * 2
print(lambdaFunc(100))
print(type(lambdaFunc))
print(type(lambda: 1))
print(foo.__name__)
print(lambdaFunc.__name__)
print()


# 内建方法Build-in-method
print(type([].append))
print(dir([].append))


class C(object):
    def foo(self): pass


c = C()
print(type(C))
print(type(c))
print(type(C.foo))  # 非绑定的类方法就是函数
print(type(c.foo))  # 绑定的类方法
print(C.foo)
print(c.foo)
