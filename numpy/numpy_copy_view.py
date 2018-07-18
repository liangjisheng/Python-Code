# -*- coding:utf-8 -*-
"""
@project = 0713-1
@file = numpy_copy_view
@author = Liangjisheng
@create_time = 2018/7/13 0013 下午 15:58
"""
import numpy as np
import time

a = np.arange(1, 7).reshape((3, 2))
a_view = a[:2]
a_copy = a[:2].copy()

a_copy[1, 1] = 0
print(a)
a_view[1, 1] = 0
print(a)
print()

# view不会复制东西, 速度快
a = np.zeros((1000, 1000))
b = np.zeros((1000, 1000))
N = 499

def f1(a):
    for _ in range(N):
        # 将下面这个view给赋值了,和`a[:] *= 2`一个意思, 从头到尾没有创建新的东西
        a *= 2

def f2(b):
    for _ in range(N):
        # b = 2*b中, 我们将b赋值给另外一个新建的b
        b = 2 * b

t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()

print('%f' % ((t1 - t0) / N))
print('%f' % ((t2 - t1) / N))
print()

# 矩阵展平, ravel返回的是一个view, flatten 返回的总是一个copy
def f3(a):
    for _ in range(N):
        a.flatten()

def f4(b):
    for _ in range(N):
        b.ravel()

t3 = time.time()
f3(a)
t4 = time.time()
f4(b)
t5 = time.time()

print('%f' % ((t4 - t3) / N))
print('%f' % ((t5 - t4) / N))
print()

print(a[:100].shape)        # (100, 1000)
print(a[::2].shape)         # (500, 1000)
