# -*- coding:utf-8 -*-
"""
@project = 0612-1
@file = numpy_r_c_
@author = Liangjisheng
@create_time = 2018/6/12 0012 下午 20:22
"""
import numpy as np

# 将切片对象沿第一轴连接 np.r_
print(np.r_[np.array([1, 2, 3]), 0, 0, np.array([4, 5, 6])])
print(np.r_[-1:1:6j, [0] * 3, 5, 6])

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
print(np.r_['-1', a, a])
print(np.r_[a, a])
print(a.shape)
print(np.array([1, 2, 3]).shape)
print(np.array([[1], [2], [3]]).shape)
print()

print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])
