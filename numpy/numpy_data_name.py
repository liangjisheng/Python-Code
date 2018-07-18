# -*- coding:utf-8 -*-
"""
@project = 0713-1
@file = numpy_data_name
@author = Liangjisheng
@create_time = 2018/7/13 0013 下午 16:30
"""
import numpy as np
import pandas as pd
import time
N = 99

# 实现用名字来索引. 这就是structured array
a = np.zeros(3, dtype=[('foo', np.int32), ('bar', np.float16)])
b = pd.DataFrame(np.zeros((3, 2), dtype=np.int32), columns=['foo', 'bar'])
b['bar'] = b['bar'].astype(np.float16)
print(a)
print(b)

def f1(a):
    for _ in range(N):
        a['bar'] *= a['foo']

def f2(b):
    for _ in range(N):
        b['bar'] *= b['foo']

t0 = time.time()
f1(a)
t1 = time.time()
f2(a)
t2 = time.time()

print(t0)
print(t1)
print(t2)
# 可以看出来, numpy明显比pandas快很多
print('%f' % ((t1 - t0) / N))
print('%f' % ((t2 - t1) / N))
