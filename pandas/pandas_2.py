# -*- coding:utf-8 -*-
"""
@project = 0601-1
@file = pandas_2
@author = Liangjisheng
@create_time = 2018/6/2 0002 下午 16:09
"""
import matplotlib.pylab as plt
import pandas as pd
import numpy as np

comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
value = pd.Series(np.concatenate([comp1, comp2]))
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))

combined = {'comp1': comp1, 'comp2': comp2}
pd_combined = pd.DataFrame(combined)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
# normed设置是否进行归一化
value.hist(bins=100, alpha=0.3, color='k', normed=True)
# 密度图也被称为KDE(kernel density estimate,核密度估计)调用plot时在kind
# 设置为'kde'就可以生成密度图
value.plot(kind='kde', style='k--')
ax2 = fig.add_subplot(2, 1, 2)
plt.scatter(comp1, comp2)
fig.show()

fig1, axes1 = plt.subplots(2, 1)
# print(data)
data.plot(kind='bar', ax=axes1[0], color='k', alpha=0.7)
data.plot(kind='barh', ax=axes1[1], color='b', alpha=0.7)
fig1.show()

plt.clf()
pd.scatter_matrix(pd_combined, diagonal='kde')
pd.scatter_matrix(pd_combined, diagonal='hist')
plt.show()
