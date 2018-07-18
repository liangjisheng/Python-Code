# -*- coding:utf-8 -*-
"""
@project = 0601-1
@file = matplotlib_1
@author = Liangjisheng
@create_time = 2018/6/2 0002 下午 15:37
"""
import matplotlib.pylab as plt
import pandas as pd
import numpy as np

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
# plt.savefig('test.jpg', bbox_inches='tight')
