# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = class_new
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 17:49
"""
class B(object):
    def __init__(self):
        print('B INIT')

    def fn(self):
        print('B fn')

class A(object):
    def __init__(self, num):
        print('A INIT', num)

    def __new__(cls, num, *args, **kwargs):
        print('NEW', num)
        if num > 10:
            return super().__new__(cls)
        return B()

    def fn(self):
        print('A fn')


# 使用__new__方法，可以决定返回那个对象，也就是创建对象之前，这个可以用于
# 设计模式的单例、工厂模式。__init__是创建对象是调用的
if __name__ == '__main__':
    a1 = A(5)
    print()
    a1.fn()
    print()

    a2 = A(20)
    print()
    a2.fn()
