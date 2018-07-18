# -*- coding:utf-8 -*-
"""
@project = 0705-1
@file = matplotlib_2
@author = Liangjisheng
@create_time = 2018/7/5 0005 下午 19:47
"""
import numpy as np
import matplotlib.pyplot as plt

# 以自然数序列作为多项式的系数，使用poly1d函数创建多项式
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
# m=1表示得到func函数的一阶导数
func1 = func.deriv(m=1)
func2 = func.deriv(m=2)      # 二阶导数
# 在-10和10之间产生30个均匀分布的值
x = np.linspace(-10, 10, 30)
y = func(x)
y1 = func1(x)
y2 = func2(x)

plt.subplot(311)        # 3行1列创建第一个子图
plt.plot(x, y, 'r-')    # 红色实线
plt.title('Polynomial')

plt.subplot(312)        # 创建第二个子图
plt.plot(x, y1, 'b^')   # 蓝色三角形
plt.title('First Derivative')   # 一阶导

plt.subplot(313)        # 创建第三个子图
plt.plot(x, y2, 'go')   # 绿色圆形
plt.title('Second Derivative')  # 二阶导

plt.xlabel('x')
plt.ylabel('y')
plt.show()
