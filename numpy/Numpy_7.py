# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_7
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 15:46
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

a = np.arange(12).reshape((3, 4))
b = a > 4
print(b)
print(a[b])
a[b] = 0
print(a)

# 第二种通过布尔来索引的方法更近似于整数索引；对数组的每个维度
# 我们给一个一维布尔数组来选择我们想要的切片
a = np.arange(12).reshape((3, 4))
b1 = np.array([False, True, True])          # first dim selection
b2 = np.array([True, False, True, False])   # second dim selection
print(a[b1, :])     # selecting rows
print(a[b1])        # same thing
print(a[:, b2])     # selecting columns
print(a[b1, b2])
print(a)
print(a[b1, 0:3])
# print(a[1:3, 2:4])
print()

import numpy.linalg as lina

a = np.array([[1., 2.],
              [3., 4.]])
print(a)
print(a.transpose())
print(lina.inv(a))      # 矩阵的逆

u = np.eye(2)
print(u)
j = np.array([[0., -1.],
              [1., 0.]])
print(j)
print(np.dot(j, j))     # matrix product

print(np.trace(u))

y = np.array([[5.],
              [7.]])

print(lina.solve(a, y))
print(lina.eig(j))
