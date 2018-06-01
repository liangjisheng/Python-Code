# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_2
@author = Liangjisheng
@create_time = 2018/5/24 0024 上午 11:27
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b ** 2)
# numpy中的sin与python内置的math.sin是不一样的，np.sin可以接受数字，序列或数组
# math.sin只能接受数字
print(10 * np.sin(a))
print(a < 35)
print()

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)            # elementwise product
print(np.dot(A, B))     # matrix product

a = np.ones((2, 3), dtype=np.int)
b = np.random.random((2, 3))       # 生成[0, 1]间均匀分布的2 x 3的矩阵
a *= 3
print(a)
b += a
print(b)
# a += b      # 类型不能转换,float64不能转换为int32
print()

# 许多非数组运算，如计算数组所有元素之和，被作为ndarray类的方法实现
a = np.random.random((2, 3))
print(a)
print(a.sum())
print(a.min())
print(a.max())
print()

# 这些运算默认应用到数组好像它就是一个数字组成的列表，无关数组的形状
# 然而，指定axis参数你可以吧运算应用到数组指定的轴上
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum())              # sum of all elements
print(b.sum(axis=0))        # sum of each column
print(b.sum(axis=1))        # sum of each row
print(b.min(axis=0))        # min of each column
print(b.min(axis=1))        # min of each row
print(b.cumsum(axis=0))     # cumulative sum along each column
print(b.cumsum(axis=1))     # cumulative sum along each row

print(b[0])
print(b[1])
print(b[2])
print(b[[0, 1]])
print(b[[0, 1], 0])
print(b[[0, 1, 2], 0])
print(b[:, 0])
print(b[[0, 1], 1])
print(b[0, [0, 1]])
