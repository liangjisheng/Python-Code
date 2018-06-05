# -*- coding:utf-8 -*-
"""
@project = 0604-1
@file = numpy_1
@author = Liangjisheng
@create_time = 2018/6/4 0004 下午 20:15
"""
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.shape)
print(a.ndim)
print()
b = np.array([[1], [2], [3]])
print(b)
print(b.shape)
print(b.ndim)
print()
c = np.array([[1, 2, 3]])
print(c)
print(c.shape)
print(c.ndim)
print()

a1 = np.tile(a, 2)
print(a1)
print(a1.shape)
print(a1.ndim)
print()

a2 = np.tile(a, (2, 3))
print(a2)
print(a2.shape)
print(a2.ndim)
print()

# 在列方向上重复[0,0]5次，默认行1次
print(np.tile([0, 0], 5))
# 在列方向上重复[0,0]1次，行1次
print(np.tile([0, 0], (1, 1)))
# 在列方向上重复[0,0]1次，行2次
print(np.tile([0, 0], (2, 1)))
print(np.tile([0, 0], (3, 1)))
# 在列方向上重复[0,0]3次，行1次
print(np.tile([0, 0], (1, 3)))
print(np.tile([0, 0], (2, 3)))
