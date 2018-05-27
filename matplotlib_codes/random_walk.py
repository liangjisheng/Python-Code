# -*- coding:utf-8 -*-
"""
@project = 0527-2
@file = random_walk
@author = Liangjisheng
@create_time = 2018/5/27 0027 下午 19:05
"""
import random
import matplotlib.pyplot as plt

class RandomWalk(object):
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步包含的点"""

        #不断漫步，直到列表达到指定的长度
        while len(self.x_value) < self.num_points:
            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = random.choice([-1, 1])
            x_distance = random.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = random.choice([-1, 1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)


if __name__ == '__main__':
    rw = RandomWalk()
    rw.fill_walk()
    print('test')
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()
