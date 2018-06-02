# -*- coding:utf-8 -*-
"""
@project = 0601-1
@file = matplotlib_2
@author = Liangjisheng
@create_time = 2018/6/2 0002 下午 15:52
"""
import matplotlib.pylab as plt
import pandas as pd
import numpy as np

fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
data_one = np.random.randn(500).cumsum()
data_two = np.random.randn(500).cumsum()
data_three = np.random.randn(500).cumsum()
time = pd.date_range('2007-01-28', periods=500, freq='D')

ax.plot(time, data_one, 'r--', label='red')
ax.plot(time, data_two, 'b.', label='blue')
ax.plot(time, data_three, 'k-', drawstyle='steps-post', label='steps-post')

ticks = ax.set_xticks(['2007-01-28', '2007-10-01', '2008-03-01'])
labels = ax.set_xticklabels(['zero', 'one', 'two'])
ax.set_title('test of multi-linestyles and xticks')
plt.legend(loc='best')
plt.show()
