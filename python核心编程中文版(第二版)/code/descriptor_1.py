# -*- coding:utf-8 -*-
"""
@project = 1
@file = descriptor_1
@author = Liangjisheng
@create_time = 2018/3/28 0028 下午 19:11
"""


class DevNull1(object):
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass


class C1(object):
    foo = DevNull1()


c1 = C1()
c1.foo = 'bar'
print('c1.foo contains:', c1.foo)
print()


class DevNull2(object):
    def __get__(self, instance, owner):
        print('Accessing attributes... ignoring')

    def __set__(self, instance, value):
        print('Attempt to assign %r... ignoring' % value)


class C2(object):
    foo = DevNull2()


c2 = C2()
c2.foo = 'bar'
x = c2.foo
print('c2.foo contains:', x)
print()


class DevNull3(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        print('Accessing [%s]... ignoring' % self.name)

    def __set__(self, instance, value):
        print('Assigning %r to [%s]... ignoring' % (value, self.name))


class C3(object):
    foo = DevNull3('foo')


c3 = C3()
c3.foo = 'bar'
x = c3.foo
print('Let us try to sneak it into c3 instance...')
c3.__dict__['foo'] = 'bar'
x = c3.foo
print('c3.foo contains:', x)
print("c3.__dict__['foo'] contains: %r" % c3.__dict__['foo'], "... why?!?")
