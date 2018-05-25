# -*- coding:utf-8 -*-
"""
@project = 2
@file = descriptor_1
@author = Liangjisheng
@create_time = 2018/3/29 0029 下午 18:52
"""

# __dict__(每个对象均具备该属性)
# 对象访问的顺序为:1.实例属性，2.类属性，3.父类属性，4__getattr()__方法


class Test(object):
    cls_var = 1

    def __init__(self):
        self.ins_val = 0


t = Test()
print(Test.__dict__.keys())     # 返回类中可见的属性
print(t.__dict__.keys())        # 返回实例中可见的属性
print(dir(Test))                # 返回类的所有属性
print(dir(t))                   # 返回实例的所有属性(比类的属性多了实例属性)

t.cls_var = 20                  # 只是在实例属性中增加了cls_var，并不影响类Test的属性cls_val
print(t.__dict__.keys())
