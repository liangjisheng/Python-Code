# -*- coding:utf-8 -*-
"""
@project = 0705-1
@file = animation
@author = Liangjisheng
@create_time = 2018/7/5 0005 下午 20:28
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)

# 绘制三个随机生成的数据集，分别用圆形、小圆点和三角形来显示。不过，我们将只
# 用随机值更新其中的两个数据集
# 我们将用不同颜色的圆形、小圆点和三角形来绘制三个数据集中的数据点
circles, triangles, dots = ax.plot(x, 'ro', y, 'g^', z, 'b.')

ax.set_ylim(0, 1)   # 设置y坐标的范围
plt.axis('off')

# 下面的函数将被定期调用以更新屏幕上的内容。我们将随机更新两个数据集中的y坐
# 标值
def update(data):
    circles.set_ydata(data[0])
    triangles.set_ydata(data[1])
    return circles, triangles

# 使用numpy生成随机数
def generate():
    while True:
        yield np.random.rand(2, N)


# 每个150毫秒更新一次
anim = animation.FuncAnimation(fig, update, generate, interval=150)
plt.show()
