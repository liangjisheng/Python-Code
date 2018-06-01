# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_6
@author = Liangjisheng
@create_time = 2018/5/25 0025 上午 10:11
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

a = np.arange(12) ** 2      # the first 12 square numbers
i = np.array([1, 1, 3, 8, 5])   # an array of indices
print(a[i])                 # the elements of a at the position i
j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
print(a[j])         # the same shape as j

# 当被索引数组a是多维的时，每一个唯一的索引数列指向a的第一维
palette = np.array([[0, 0, 0],          # black
                    [255, 0, 0],        # red
                    [0, 255, 0],        # green
                    [0, 0, 255],        # blue
                    [255, 255, 255]     # white
                    ])
image = np.array([[0, 1, 2, 0],         # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])           # the (2, 4, 3) color image
print()

# 我们也可以给出不不止一维的索引，每一维的索引数组必须有相同的形状
a = np.arange(12).reshape(3, 4)
print(a)
i = np.array([[0, 1],           # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],           # indices for the second dim
              [3, 3]])
print(a[i, j])                  # i and j must have equal shape
print(a[i, 2])
print(a[:, j])
l = [i, j]
print(a[l])         # equivalent to a[i, j]
print()

# 另一个常用的数组索引用法是搜索时间序列最大值
time = np.linspace(20, 145, 5)
print(time)
data = np.sin(np.arange(20)).reshape(5, 4)
print(data)

ind = data.argmax(axis=0)           # index of the maxima for each series
print(ind)
time_max = time[ind]
print(time_max)
data_max = data[ind, list(range(data.shape[1]))]    # => data[ind[0], 0], data[ind[1], 1]...
print(data_max)
print(data.max(axis=0))
print(all(data_max == data.max(axis=0)))
print()

# 使用数组索引作为目标来赋值
a = np.arange(5)
print(a)
a[[1, 3, 4]] = 0
print(a)
a[[0, 0, 2]] = [1, 2, 3]
print(a)
a = np.arange(5)
a[[0, 0, 2]] += 1
print(a)
