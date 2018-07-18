# -*- coding:utf-8 -*-
"""
@project = 0705-1
@file = matplotlib_1
@author = Liangjisheng
@create_time = 2018/7/5 0005 下午 19:39
"""
import numpy as np
import matplotlib.pyplot as plt

# 以自然数序列作为多项式的系数，使用poly1d函数创建多项式
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
# m=1表示得到func函数的一阶导数
func1 = func.deriv(m=1)
# 在-10和10之间产生30个均匀分布的值
x = np.linspace(-10, 10, 30)
y = func(x)
y1 = func1(x)

plt.plot(x, y, 'ro', x, y1, 'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
