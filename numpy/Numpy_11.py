# -*- coding:utf-8 -*-
"""
@project = 0529-1
@file = numpy_1
@author = Liangjisheng
@create_time = 2018/5/29 0029 下午 17:57
"""
import numpy as np

# 将切片对象沿第二个轴（按列）转换为连接
print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])

x = np.array([[1, 2],
              [3, 4]])
y = np.array([[1, 2],
              [3, 4]])

# numpy.quiver 将多维数组降低为一位数组，和 numpy.flatten 实现的功能一样。
# 两者的区别在于返回 copy 还是返回视图 view，numpy.flatten 返回一份拷贝，
# 对拷贝所做的修改不会影响原始矩阵,而numpy.ravel()返回的是视图view,会影响原始矩阵
print(x.flatten())
x.flatten()[1] = 100
print(x)

print(y.ravel())
y.ravel()[1] = 100
print(y)
