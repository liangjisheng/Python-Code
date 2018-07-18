# -*- coding:utf-8 -*-
"""
@project = 0527-2
@file = matplotlib_2
@author = Liangjisheng
@create_time = 2018/5/27 0027 下午 18:28
"""
import matplotlib.pyplot as plt

def simple_test1():
    """绘制简单的图表"""
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    # 设置图表的标题，并给坐标轴加上标签
    plt.title('Square Number', fontsize=24)
    plt.xlabel('Value', fontsize=24)
    plt.ylabel('Square of Value', fontsize=24)

    # 设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.show()

    # 保存在当前的目录下，文件名为squares_plot.png
    # plt.savefig('squares_plot.png', bbox_inches='tight')

def plot_scatter():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    # s控制点的大小
    plt.scatter(x_values, y_values, s=100)

    plt.title("Square Number", fontsize=24)
    plt.xlabel("Value", fontsize=24)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', labelsize=14)

    plt.show()

def plot_scatter1():
    x_value = list(range(1, 1001))
    y_value = [x ** 2 for x in x_value]

    # 点的颜色c=(0,0,1,0.5), edgecolors='red'点的边缘颜色
    plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)
    # 设置图表的标题 并给坐标轴加上标签
    plt.title("Square Number", fontsize=24)
    plt.xlabel("Value", fontsize=24)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


if __name__ == '__main__':
    # simple_test1()
    # plot_scatter()
    plot_scatter1()
