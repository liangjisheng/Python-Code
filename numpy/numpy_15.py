# -*- coding:utf-8 -*-
"""
@project = 0612-1
@file = numpy_3
@author = Liangjisheng
@create_time = 2018/6/13 0013 下午 18:11
"""
import numpy as np

x = np.arange(0, 6)
print(x)
print(x.reshape((2, 3)))
print(x.reshape((2, 3)).reshape((3, 2)))
y = np.array([[1, 1, 1], [1, 1, 1]])
x = x.reshape(y.shape)
print(x)
print(x.flatten())      # [0 1 2 3 4 5]     # 返回的是拷贝
print(x.ravel())        # [0 1 2 3 4 5]     # 返回的是视图
print(x)

# 维度大小自动推导
arr = np.arange(15)
print(arr.reshape((5, -1)))
print()

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([x, y], axis=0))       # 竖直组合
# print(x.sum(axis=0))
print(np.concatenate([x, y], axis=1))       # 水平组合
print()

print(np.vstack((x, y)))        # 垂直堆叠:相当于垂直组合
print(np.hstack((x, y)))        # 水平堆叠:相当于水平组合

# dstack:按深度堆叠
print(np.split(x, x.shape[0], axis=0))
print(np.split(x, x.shape[1], axis=1))
print()

# 堆叠辅助类
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print(arr1)
print(arr2)
# np.r_用于按行堆叠
print(np.r_[arr1, arr2])
# np.c_用于按列堆叠
print(np.c_[arr1, arr2])
print()

# 切片直接转换为数组
print(np.c_[1:6, -10:-5])
print(np.r_[1:6, -10:-5])
