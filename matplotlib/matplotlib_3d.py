# -*- coding:utf-8 -*-
"""
@project = 0705-1
@file = matplotlib_3d
@author = Liangjisheng
@create_time = 2018/7/5 0005 下午 20:13
"""
# 绘制一个简单的三维函数
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 我们将使用meshgrid函数创建一个二维的坐标网格
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2

# 我们将指定行和列的步幅，以及绘制曲面所用的色彩表(color map)
# 步幅决定曲面上“瓦片”的大小，而色彩表的选择取决于个人喜好
ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.YlGnBu_r)
plt.show()
