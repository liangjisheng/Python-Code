# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = class_call
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 17:44
"""
# 为了能让对象实例能被直接调用，需要实现__call__方法
class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num, *args, **kwargs):
        print('call:', num + self.__a + self.__b)


if __name__ == '__main__':
    a1 = A(10, 20)
    a1.myprint()
    a1(30)
