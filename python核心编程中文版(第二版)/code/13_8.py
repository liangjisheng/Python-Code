# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_8
@author = Liangjisheng
@create_time = 2018/3/27 0027 下午 20:06
"""
# 包装类例子


class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return repr(self.__data)

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, item):
        return getattr(self.__data, item)


wrappedComplex = WrapMe(3.5 + 4.2j)
print(wrappedComplex)
# 当引用一个属性时，Python 解释器将试着在局部名称空间中查找那个名字，比如一个
# 自定义的方法或局部实例属性。如果没有在局部字典中找到，则搜索类名称空间，以防一个类属性
# 被访问。最后，如果两类搜索都失败了，搜索则对原对象开始授权请求，此时，__getattr__()会被调用
print(wrappedComplex.real)          # 对属性的访问通过getattr()方法，授权给对象
print(wrappedComplex.imag)
print(wrappedComplex.conjugate())
print(wrappedComplex.get())
print()

wrappedList = WrapMe([123, 'foo', 45.67])
wrappedList.append('bar')
wrappedList.append(123)
print(wrappedList)
print(wrappedList.index(45.67))
print(wrappedList.count(123))
print(wrappedList.pop())
print(wrappedList)
