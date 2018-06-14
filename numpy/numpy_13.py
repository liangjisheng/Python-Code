# -*- coding:utf-8 -*-
"""
@project = 0612-1
@file = numpy_1
@author = Liangjisheng
@create_time = 2018/6/13 0013 上午 11:40
"""
import numpy as np

test1 = np.array([[5, 10, 15],
                  [20, 25, 30],
                  [35, 40, 45]])
print(test1.sum())
print(test1.max())
print(test1.min())
print(test1.mean())
print()

print(test1.sum(axis=0))    # 矩阵列求和
print(test1.sum(axis=1))    # 矩阵行求和

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(a * b)    # 对应位置元素相乘
print(a.dot(b))     # 矩阵乘法
print(np.dot(a, b))     # 矩阵乘法
print(a ** 2)       # 对应元素平方
print(a.ravel())    # 平坦化数组，二维n行n列转换为一维数组
print()

print(np.vstack((a, b)))    # 矩阵按行拼接
print(np.hstack((a, b)))    # 矩阵按列拼接

a = np.floor(10 * np.random.random((2, 12)))
print(a)
print(np.hsplit(a, 3))      # 按列分割，分割成3列
print('---')
# 参数(3, 4)为在维度3前面也就是第4列前切一下，在维度4也就是第5列前面切一下
print(np.hsplit(a, (3, 4)))

a = np.floor(10 * np.random.random((12, 2)))
print(a)
print(np.vsplit(a, 3))
print('---')
print(np.vsplit(a, (3, 5)))
