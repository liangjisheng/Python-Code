# -*- coding:utf-8 -*-
"""
@project = 0705-1
@file = matplotlib_3d_1
@author = Liangjisheng
@create_time = 2018/7/5 0005 下午 20:23
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111)

# 我们将使用meshgrid函数创建一个二维的坐标网格
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2

# Matplotlib中的等高线3D绘图有两种风格——填充的和非填充的。我们可以使用contour函
# 数创建一般的等高线图。对于色彩填充的等高线图，可以使用contourf绘制
# ax.contour(x, y, z)   # 不填充
ax.contourf(x, y, z)    # 填充
plt.show()
