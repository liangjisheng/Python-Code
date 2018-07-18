# -*- coding:utf-8 -*-
"""
@project = 0529-1
@file = matplotlib_4
@author = Liangjisheng
@create_time = 2018/5/29 0029 下午 19:53
"""
import numpy as np
import matplotlib.pyplot as plt

x_min = 0.0
x_max = 1.0
y_min = 0.0
y_max = 1.0

# create data grid
h = .01
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# create classification
grid = np.c_[xx.flatten(), yy.flatten()]
print(grid.shape)

pred = np.zeros((grid.shape[0], 1))

for i in range(0, len(grid)):
    if i >= (grid.shape[0] / 2):
        pred[i] = 1

# order='F'表示按列重新排列
pred = pred.reshape(xx.shape, order='F')
print(pred[:10])

# plot figure
plt.style.use('ggplot')
plt.figure()
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.pcolormesh(xx, yy, pred)
plt.show()
