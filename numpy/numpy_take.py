# -*- coding:utf-8 -*-
"""
@project = 0713-1
@file = numpy_take
@author = Liangjisheng
@create_time = 2018/7/13 0013 下午 16:17
"""
import numpy as np
import time

a = np.random.rand(1000000, 10)
N = 499
indices = np.random.randint(0, 1000000, size=10000)

def f1(a):
    for _ in range(N):
        # 拷贝a中数据
        _ = np.take(a, indices, axis=0)

def f2(b):
    for _ in range(N):
        # # 拷贝b中数据
        _ = b[indices]

# 返回的应该是从某个时间点到现在为止所经过的秒数
t0 = time.time()
f1(a)
t1 = time.time()
f2(a)
t2 = time.time()

print(t0)
print(t1)
print(t2)
print('%f' % ((t1 - t0) / N))
print('%f' % ((t2 - t1) / N))
