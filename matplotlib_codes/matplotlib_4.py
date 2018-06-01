# -*- coding:utf-8 -*-
"""
@project = 0529-1
@file = matplotlib_3
@author = Liangjisheng
@create_time = 2018/5/29 0029 下午 17:44
"""
import numpy as np
import matplotlib.pyplot as plt

# 根据给定的坐标向量创建坐标矩阵。在上面的例子中，所得到的是 X 轴上 [0, 1, 2] 和 Y
# 轴上 [0, 1] 构成的一个 3x2 的网格，共有 6 个点。返回的两个值中的 x 是这 6 个点
# 在 X 轴上的投影， y 则是这 6 个点在 y 轴的投影
# 通常我们将 meshgrid 用于绘制图形
# x, y = np.meshgrid(np.arange(0, 3), np.arange(0, 2))
# print(type(x))
# print(x.shape)

x, y = np.meshgrid(np.arange(-1, 1, 0.01), np.arange(-1, 1, 0.01))
contor = np.sqrt(x ** 2 + y ** 2)

plt.style.use('ggplot')
plt.figure()
plt.imshow(contor)
plt.colorbar()
plt.grid(False)
plt.show()
