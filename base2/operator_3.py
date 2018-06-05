# -*- coding:utf-8 -*-
"""
@project = 0604-1
@file = operator_3
@author = Liangjisheng
@create_time = 2018/6/5 0005 下午 20:07
"""
import operator as op

# operator模块中的函数通过相应操作的标准Python接口完成工作，
# 所以它们不仅适用于内置类型，还适用于用户自定义类型
class MyObj(object):
    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val
        return

    def __str__(self):
        return "MyObj(%s)" % self.val

    def __lt__(self, other):
        return self.val < other.val

    def __add__(self, other):
        return MyObj(self.val + other.val)

a = MyObj(1)
b = MyObj(2)
print(op.lt(a, b))
print(op.add(a, b))
print()

# operator 模块还包含一些函数用来测试映射、数字和序列类型的API兼容性
class NoType(object):
    pass

class MultiType(object):
    def __len__(self):
        return 0

    def __getitem__(self, item):
        return 'mapping'

    def __int__(self):
        return 0

o = NoType()
t = MultiType()

# AttributeError: module 'operator' has no attribute 'isMappingType'
# for func in [op.isMappingType, op.isNumberType, op.isSequenceType]:
    # print("%s(o):" % func.__name__, func(o))
    # print("%s(t):" % func.__name__, func(t))

