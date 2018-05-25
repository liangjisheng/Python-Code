# -*- coding:utf-8 -*-
"""
@project = 2
@file = descriptor_6
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 21:00
"""


class SimpleDesc(object):
    def __init__(self):
        print('__init__')
        self.result = None

    def __get__(self, instance, owner):
        return self.result - 10

    def __set__(self, key, value):
        self.result = value + 3
        print(self.result)

    def __del__(self):
        pass


class A(object):
    foo = SimpleDesc()


a = A()         # __init__
a.foo = 13      # 16,赋值时，调用__set__()打印16
print(a.foo)    # 6，调用__get__()
