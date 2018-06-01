# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_10
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 19:19
"""
import numpy as np

a = np.arange(10).reshape(2, 5)
print(a)
ixgrid = np.ix_([0, 1], [2, 4])
print(ixgrid)
print(ixgrid[0])
print(ixgrid[1])
print(ixgrid[0].shape)
print(ixgrid[1].shape)
print(a[ixgrid])
print()

ixgrid = np.ix_([True, True], [2, 4])
print(ixgrid)
print(a[ixgrid])

ixgrid = np.ix_([True, True], [False, False, True, False, True])
print(ixgrid)
print(a[ixgrid])
