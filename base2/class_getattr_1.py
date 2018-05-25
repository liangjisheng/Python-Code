# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = class_getattr_1
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 19:15
"""
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('default', str(args[0]))

    # 添加代码，使得没有定义的方法都调用mydefault函数, item为未找到的属性的名字
    def __getattr__(self, item):
        print(type(item))
        print(item)
        return self.mydefault


if __name__ == '__main__':
    a1 = A(10, 20)
    # 当fn1方法传入参数时，我们可以给mydefault方法增加一个*args不定参数来兼容
    a1.fn1(33)
    a1.fn2('hello')
    a1.fn3(10)




