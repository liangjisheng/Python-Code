# -*- coding:utf-8 -*-
"""
@project = 1
@file = RoundFloat2
@author = Liangjisheng
@create_time = 2018/3/26 0026 下午 19:47
"""


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a float'
        self.value = round(val, 2)

    def __str__(self):
        # return str(self.value)
        return "%.2f" % self.value

    # __str__中的代码是一个对象，同所有对象一样，引用可以指向他们
    __repr__ = __str__
    # def __repr__(self):
        # return str(self.value)


rfm = RoundFloatManual(4.2)
print(str(rfm))
print(repr(rfm))
