# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_4
@author = Liangjisheng
@create_time = 2018/5/24 0024 下午 20:44
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

a = np.floor(10 * np.random.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())    # flatten the array
a.shape = (6, 2)
print(a)
print(a.transpose())
a.resize((2, 6))
print(a)
print()

# 组合(stack)不同的数组
a = np.floor(10 * np.random.random((2, 2)))
print(a)
b = np.floor(10 * np.random.random((2, 2)))
print(b)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

# 函数column_stack以列将一维数组合成二维数组，它等同与vstack对一维数组
print(np.column_stack((a, b)))

a = np.array([4., 2.])
b = np.array([2., 8.])
print(a[:, np.newaxis])     # This allows to have a 2D columns vector
print(np.column_stack((a[:, np.newaxis], b[:, np.newaxis])))
print(np.vstack((a[:, np.newaxis], b[:, np.newaxis])))  # The behavior of vstack is different

# 在复杂情况下，r_[]和c_[]对创建沿着一个方向组合的数很有用，它们允许范围符号(":"):
print(np.r_[1:4, 0, 4])
print()

# 将一个数组分割(split)成几个小数组
# 使用hsplit你能将数组沿着它的水平轴分割，或者指定返回相同形状数组的个数，或者指定在哪些列后发生分割:
# vsplit沿着纵向的轴分割，array split允许指定沿哪个轴分割
a = np.floor(10 * np.random.random((2, 12)))
print(a)
print(np.hsplit(a, 3))
print(np.hsplit(a, (3, 4)))
