# -*- coding:utf-8 -*-
"""
@project = 1
@file = numstr
@author = Liangjisheng
@create_time = 2018/3/27 0027 下午 18:48
"""

import operator


class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        # 使用%r相当于调用repr(),使得输出的字符串带有单引号，使用%s没有单引号
        return '[%d::%r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise TypeError('Illegal argument type for built-in operator')

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __nonzero__(self):
        """False if both are"""
        return self.__num and 0 == len(self.__string)


a = NumStr(3, 'foo')
print(a)
b = NumStr()
print(b)
c = NumStr(string='boo')
print(c)
d = NumStr(1)
print(d)

print(a + a)
print(a * 2)

if a:
    print('not False')
else:
    print('False')

if b:
    print('not False')
else:
    print('False')
