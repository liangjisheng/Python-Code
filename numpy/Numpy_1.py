# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_1
@author = Liangjisheng
@create_time = 2018/5/24 0024 上午 10:02
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

x = np.array([2, 3, 1, 0])
print(x)
x = np.array([[1, 2.0], [0, 0], (1+1j, 3.)])    # note mix of tuple and lists
print(x)

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.arange(10))
print(np.arange(2, 10, dtype=np.float))
print(np.arange(2, 3, 0.1))

# linspace()将以指定数量的元素创建数组，并平分开始值和结束值
print(np.linspace(1., 4., 6))
# indices()将创建数组的集合(用一维数组来模拟高维数组),每一维都有表示它的变量
print(np.indices((3, 3)))
print()

a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)
print(a.dtype)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
print()

# 数组类型可以在创建时显示指定
a = np.array([2, 3, 4])
print(a)
print(a.dtype)
print(type(a))
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
print(type(b))
c = np.array([[1, 2], [3, 4]], dtype=np.complex)
print(c)
print(type(c))
# 函数empty创建一个内容随机并且依赖与内存状态的数组。默认创建的数组类型(dtype)都是float64
print(np.empty((2, 3)))
