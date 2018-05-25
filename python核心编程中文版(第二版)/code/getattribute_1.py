# -*- coding:utf-8 -*-
"""
@project = 1
@file = getattribute_1
@author = Liangjisheng
@create_time = 2018/3/28 0028 下午 18:40
"""


class Test(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('said by:', self.name)

    def __getattribute__(self, item):
        print('访问了特性:', item)
        return object.__getattribute__(self, item)


test = Test('asdf')
print(test.name)
print()
test.hello()
print()


class Test1(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('said by:', self.name)

    def method_1(self, name):
        if name == self.name:
            print('yes')
        else:
            print('no')


class WrapTest1(object):
    def __init__(self, test1):
        self._test1 = test1

    def __getattr__(self, item):
        if item == 'hello':
            print('调用hello方法了')
        elif item == 'method_1':
            print('调用method_1方法了')
        # 这里通过__getattr__方法，将所有的特性的访问都路由给了内部的_test1对象
        return getattr(self._test1, item)


test1 = WrapTest1(Test1('xxxx'))
test1.hello()
test1.method_1('xxxx')
test1.method_1('xxxz')
