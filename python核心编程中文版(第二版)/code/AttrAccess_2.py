# -*- coding:utf-8 -*-
"""
@project = 2
@file = AttrAccess_2
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 20:41
"""


class Test(object):
    def __init__(self):
        self.count = 0

    def __setattr__(self, key, value):
        print('__setattr__')
        self.count += 1


# 会报AttributeError异常，因为执行__init__()时，给属性count赋值，此时会调用__setattr__()
# 而此时__init__()尚未完成，并不存在count属性，因此导致AttributeError错误
# t = Test()

# 改变上面的属性赋值
class Test1(object):
    def __setattr__(self, key, value):
        print('__setattr__ been called')
        super().__setattr__(key, value)
        # 不能再里面这样写self.key = value,这样会导致无穷递归下去，直到栈溢出


t = Test1()
t.x = 1


# 没有找到属性时访问__getattr__()
class D(object):
    def __getattr__(self, item):
        return item
        # return self.item，这样写会造成无限递归，直到栈溢出


d = D()
print(d.foo, type(d.foo))
d.foo = 15
print(d.foo)
