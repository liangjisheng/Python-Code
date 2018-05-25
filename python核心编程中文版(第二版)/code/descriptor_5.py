# -*- coding:utf-8 -*-
"""
@project = 2
@file = descriptor_5
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 19:32
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


class TestDesc(object):
    _x = Desc('x')

    def __init__(self, x):
        self._x = x


t = TestDesc(10)
# 只定义一个__get__()方法，为非数据描述符，优先级低于实例属性，所以此处没有调用__get__()
# 一个类如果只定义了__get__()方法，而没有定义__set__(),__delete__()方法，则认为是非数据描述符
# 反之则成为数据描述符
t._x

# 最后在这里总结下属性查询优先级
# 1.__getattribute__(),无条件调用
# 2.数据描述符:由1触发调用(若人为的重载了该 __getattribute__() 方法，可能会调职无法调用描述符)
# 3.实例对象的字典(若与描述符对象同名，会被覆盖)
# 4.类的字典
# 5.非数据描述
# 6.父类的字典
# 7.__getattr__()方法
