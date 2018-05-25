# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = property_1
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 11:50
"""
# python中内置了三个装饰器，都是跟class相关，staticmethod, classmethod,和property
# staticmethod没有self参数，使用类直接调用
# classmethod与成员方法的区别在于所接受的第一个参数不是self(类实例的指针),而是cls(当前类的具体类型)


class Foo(object):
    def __init__(self, var):
        super(Foo, self).__init__()
        self._var = var

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, var):
        self._var = var


foo = Foo('var 1')
# property装饰器可以实现对方法的调用转化为使用类实例对属性的访问
print(foo.var)

# var.setter装饰器对属性的赋值转换成对方法的调用
foo.var = 'var 2'
print(foo.var)
