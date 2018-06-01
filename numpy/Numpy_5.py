# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_5
@author = Liangjisheng
@create_time = 2018/5/25 0025 上午 9:57
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

a = np.arange(12)
b = a
print(b is a)
b.shape = 3, 4
print(a.shape)
print(a)

# 视图(view)和浅复制
# 不同的数组对象分享同一个数据。视图方法创造一个新的数组对象指向同一数据
c = a.view()
print(c is a)
print(c.base is a)      # c is a view of the data owned by a
print(c.flags.owndata)
c.shape = 2, 6
print(a.shape)      # (3, 4)
c[0, 4] = 1234      # a's data changes
print(a)

# 切片数组返回它的一个视图：
s = a[:, 1:3]
s[:] = 10
print(a)

# 深复制, 这个复制方法完全复制数组和它的数据
d = a.copy()
print(d is a)
print(d.base is a)
d[0, 0] = 9999
print(a)
