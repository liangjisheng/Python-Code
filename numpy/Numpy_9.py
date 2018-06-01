# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_9
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 17:34
"""
import numpy as np
import pylab

# build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
# plot a normalized histogram with 50 bins
pylab.hist(v, bins=50, normed=1)        # matplotlib version (plot)
pylab.show()

# Compute the histogram with numpy and then plot it
# n表示每个面元里的个数占总数的比例
# bins表示面元范围
(n, bins) = np.histogram(v, bins=50, normed=True)       # Numpy version (no plot)
# print(type(n))
# print(n.shape)
# print(n)
# print(type(bins))
# print(bins.shape)
# print(bins)
# print(len(bins))      # 51
# print(len(bins[:-1]))
# print(len(bins[1:]))
pylab.clf()
pylab.plot(.5*(bins[1:] + bins[:-1]), n)
pylab.show()
