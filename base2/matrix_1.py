# -*- coding:utf-8 -*-
"""
@project = 0702-1
@file = matrix_1
@author = Liangjisheng
@create_time = 2018/7/2 0002 下午 18:57
"""
import numpy as np

A = np.mat('1 2 3; 4 5 6; 7 8 9')
print(A)
print(type(A))
print(A.T)      # 转置
print('Inverse A')      # 逆矩阵
print(A.I)
print()

B = np.mat(np.arange(9).reshape(3, 3))
print(B)
print()

a = np.eye(2)       # 单位阵
b = 2 * a
print(a)
print(b)
# bmat(分块矩阵)
print(np.bmat('a b; a b'))
