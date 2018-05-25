# -*- coding:utf-8 -*-
"""
@project = 2
@file = descriptor_2
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 19:00
"""


class Desc(object):

    def __get__(self, instance, owner):
        print('__get__...')
        print('self: \t\t', self)
        print('instance: \t', instance)
        print('owner: \t', owner)
        print('='*40, '\n')

    def __set__(self, instance, value):
        print('__set__...')
        print('self: \t\t', self)
        print('instance: \t', instance)
        print('value: \t', value)
        print('='*40, '\n')


class TestDesc(object):
    x = Desc()          # x为描述符作为类属性


print(TestDesc.__dict__)
t = TestDesc()
# 访问时，实例属性没找到x，去类属性中去找，找到了；然后判断x是一个描述符，将TestDesc.x的访问转化为
# TestDesc.__dict__['x'].__get__(t, TestDesc)
t.x
print()
t.x = 10
