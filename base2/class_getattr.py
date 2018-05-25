# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = class_getattr
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 17:59
"""
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self):
        print('default')

    # 添加代码，使得没有定义的方法都调用mydefault函数
    def __getattr__(self, item):
        print(type(item))
        print(item)
        return self.mydefault


if __name__ == '__main__':
    a1 = A(10, 20)
    a1.fn1()
