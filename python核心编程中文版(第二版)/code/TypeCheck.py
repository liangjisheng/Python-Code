# -*- coding:utf-8 -*-
"""
@project = 0330-1
@file = TypeCheck
@author = Liangjisheng
@create_time = 2018/3/30 0030 下午 18:30
"""


class A(object):
    def __init__(self, a):
        self.__x = a

    @property
    def x(self):
        # assert False, 'hi one'
        print('property x')
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, str):
            assert False, 'hi two'


a = A(30)
# 如果x作为正常的函数，print()会输出函数的名称和地址，但加上property属性的话
# 访问x就会调用对应的函数，可以在这个函数中做一些自己想做的工作
print(a.x)
# 赋值的时候调用x.setter对应的函数
a.x = 20
