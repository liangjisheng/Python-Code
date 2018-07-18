# -*- coding:utf-8 -*-
"""
@project = 0713-1
@file = numpy_array
@author = Liangjisheng
@create_time = 2018/7/13 0013 下午 15:39
"""
import numpy as np
import time

# 在 Numpy 中, 创建2D Array的默认方式是"C-type"以row为主在内存中排列,
# 而如果是"Fortran"的方式创建的, 就是以column为主在内存中排列.
row_major = np.zeros((10, 10), order='C')   # C-type
col_major = np.zeros((10, 10), order='F')   # Fortran

# 在Numpy中的矩阵合并等,都是发生在一维空间里,不是我们想象的二维空间中
a = np.zeros((200, 200), order='C')
b = np.zeros((200, 200), order='F')
N = 15000

def f1(a):
    for _ in range(N):
        np.concatenate((a, a), axis=0)

def f2(b):
    for _ in range(N):
        np.concatenate((b, b), axis=0)

t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()

print(t0)
print(t1)
print(t2)
print((t1 - t0) / N * 1000000)
print((t2 - t1) / N * 1000000)

