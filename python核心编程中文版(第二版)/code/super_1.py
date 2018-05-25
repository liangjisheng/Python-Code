# -*- coding:utf-8 -*-
"""
@project = 0330-1
@file = super_1
@author = Liangjisheng
@create_time = 2018/3/30 0030 下午 18:13
"""


class A(object):
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        # 在python2.2版本之前，子类的某个方法中调用父类的某个方法，
        # 需要使用非绑定的类方法(用类名来引用的方法)，在参数列表中，引入待绑定的对象(self)
        # 达到调用父类方法的目的
        # 这样做的缺点是，当一个子类的父类发生变化时（如类B的父类由A变为C时），
        # 必须遍历整个类定义，把所有的通过非绑定的方法的类名全部替换过来
        A.__init__(self)
        print('leave B')


b = B()
print()


class A1(object):
    def __init__(self):
        print('enter A1')
        print('leave A1')


class B1(A1):
    def __init__(self):
        print('enter B1')
        # python2.2版本及其后可以使用super()
        super(B1, self).__init__()
        print('leave B1')


b1 = B1()
