# -*- coding:utf-8 -*-
"""
@project = 0330-1
@file = super_2
@author = Liangjisheng
@create_time = 2018/3/30 0030 下午 18:43
"""


class Base(object):
    def __init__(self):
        print('enter Base')
        print('leave Base')


class A(Base):
    def __init__(self):
        print('enter A')
        super(A, self).__init__()
        print('leave A')


class B(Base):
    def __init__(self):
        print('enter B')
        super(B, self).__init__()
        print('leave B')


class C(A, B):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')


c = C()
# 每定义一个类，python会计算出一个方法解析顺序(Method Resolution Order, MRO)列表，
# 它代表了类继承的顺序
print(C.mro())

# 事实上，super和父类没有实质性的关联
# super(cls, inst)获得cls在inst的MRO列表中的下一个类
# super工作原理如下
# def super(cls, inst):
    # mro = inst.__class__.mro()
    # return mro[mro.index(cls) + 1]
