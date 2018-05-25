# -*- coding:utf-8 -*-
"""
@project = 2
@file = descriptor_4
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 19:22
"""


class Desc(object):
    def __init__(self, name):
        self.name = name
        print('__init__(): name =', self.name)

    def __get__(self, instance, owner):
        print('__get__()...')
        print('self:', self)
        print('instance:', instance)
        print('owner:', owner)
        return self.name

    def __set__(self, instance, value):
        self.value = value


class TestDesc(object):
    _x = Desc('x')

    def __init__(self, x):
        self._x = x     # 这行代码并没有执行，因为描述符覆盖了实例属性_x


t = TestDesc(10)
# 正常来说，t._x会去调用__getattribute__()方法，然后找到实例属性就结束了
# 但当python解释器发现实例对象的字典中，有与描述符同名的属性时，描述符优先，会覆盖掉实例属性
t._x
print(t.__dict__)   # {}没有任何实例属性，描述符会覆盖掉实例属性
print(TestDesc.__dict__)

