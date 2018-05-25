# -*- coding:utf-8 -*-
"""
@project = 2
@file = descriptor_3
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 19:14
"""


class Desc(object):
    def __init__(self, name):
        self.name = name
        # print('__init__(): name =', name)

    def __get__(self, instance, owner):
        print('__get__...')
        print('self: \t\t', self)
        print('instance: \t', instance)
        print('owner: \t', owner)
        print('name =', self.name)
        print('='*40, '\n')


class TestDesc(object):
    x = Desc('x')

    def __init__(self):
        self.y = Desc('y')


t = TestDesc()
t.x
# 因为调用 t.y 时刻，首先会去调用TestDesc(即Owner）的 __getattribute__() 方法，该方法将 t.y 转化为
# TestDesc.__dict__['y'].__get__(t, TestDesc)， 但是呢，实际上 TestDesc 并没有 y这个属性，y 是属于实例对象的，
# 所以，只能忽略了.说明了描述符只能用作类属性
t.y
