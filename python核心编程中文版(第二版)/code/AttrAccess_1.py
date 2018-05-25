# -*- coding:utf-8 -*-
"""
@project = 2
@file = AttrAccess_1
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 20:23
"""


class Test(object):
    def __getattribute__(self, item):
        print('__getattribute__')
        super().__getattribute__(item)
        # 下面两行代码同样起作用
        # super(Test, self).__getattribute__(item)
        # object.__getattribute__(self, item)

    def __getattr__(self, item):
        print('__getattr__')

    def __setattr__(self, key, value):
        print('__setattr__')

    def __delattr__(self, item):
        print('__delattr__')


t = Test()
# 1.首先调用__getattribute__()方法，默认隐含调用，无论何时都会调用此方法
# 2.去实例属性中查找
# 3.去类属性中查找
# 4.去父类属性中查找
# 5.如果以上都没有找到，则调用__getattr__(),执行内部命令，如果为重载,直接报AttributeError
# 一旦重载了__getattribute__()方法,如果找不到属性，则必须手动加入第4步，否则无法进入第5步__getattr__()
t.x
t.x = 10
del t.x
