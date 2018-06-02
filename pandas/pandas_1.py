# -*- coding:utf-8 -*-
"""
@project = 0601-1
@file = pandas_1
@author = Liangjisheng
@create_time = 2018/6/2 0002 下午 15:59
"""
# 除了matplotlib， pandas的Series和DataFrame都具有许多根据其自身数据组织特点
# 来创建标准绘图的高级绘图方法
import matplotlib.pylab as plt
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(100), index=np.arange(0, 100))
s.plot()
plt.show()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                  columns=['a', 'b', 'c', 'd'],
                  index=np.arange(0, 100, 10))
plt.clf()
df.plot()
plt.show()
