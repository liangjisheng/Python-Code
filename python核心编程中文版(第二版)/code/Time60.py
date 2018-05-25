# -*- coding:utf-8 -*-
"""
@project = 1
@file = Time60
@author = Liangjisheng
@create_time = 2018/3/26 0026 下午 20:27
"""


class Time60(object):
    """class Time60"""

    def __init__(self, hr, min):
        """Time60 constructor - takes hours and minutes"""
        self.hr = hr
        self.min = min

    def __str__(self):
        """Time60 - string representation"""
        return '%d:%d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        """Time60 - overloading the addition operator"""
        # self.__class__与Time60相同，一般情况下不直接写类名，而是使用__class__属性
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        """原位加法，支持增量赋值，类似于obj1 += obj2, 要求是必须返回self
        Time60 - overloading in-place addition"""
        self.hr += other.hr
        self.min += other.min
        return self


mon = Time60(10, 30)
tue = Time60(11, 15)
print(mon)
print(id(mon))
print(tue)
print(mon + tue)
mon += tue
print(mon)
print(id(mon))
