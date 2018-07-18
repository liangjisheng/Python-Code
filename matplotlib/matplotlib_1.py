# -*- coding:utf-8 -*-
"""
@project = 0527-2
@file = matplotlib_1
@author = Liangjisheng
@create_time = 2018/5/27 0027 下午 17:33
"""
import matplotlib.pyplot as plt
import numpy as np


def simple_test():
    plt.figure(1)       # 创建图表1
    plt.figure(2)       # 创建图表2
    plt.show()          # 显示所有图表

def simple_test2():
    plt.figure(1)       # 创建图表1
    plt.subplot(223)    # 创建2*2的图表矩阵，绘制的子图为矩阵中的3序号
    plt.show()

def simple_test3():
    plt.figure(1, dpi=50)       # 创建图表1，dpi为设置图表的大小，默认dpi=80
    plt.subplot(221)
    plt.subplot(222)
    plt.subplot(223)
    plt.subplot(224)
    plt.show()

def simple_test4():
    """在多个表中创建子图"""
    plt.figure(1, dpi=50)
    plt.subplot(111)    # 在图表1中创建子图
    plt.figure(2, dpi=50)
    plt.subplot(221)
    plt.show()

def plot_sin():
    plt.figure(1, dpi=50)
    x = np.linspace(-np.pi, np.pi, 100)
    plt.plot(x, np.sin(x))
    plt.show()

def plot_sca():
    """sca()函数，选择子图"""
    plt.figure(1, dpi=50)
    ax1 = plt.subplot(211)      # 创建子图ax1
    ax2 = plt.subplot(212)      # 创建子图ax2

    x = np.linspace(0, 10, 100)
    plt.sca(ax1)        # 选择子图ax1
    plt.plot(x, np.exp(x))

    plt.sca(ax2)
    plt.plot(x, np.sin(x))

    plt.show()

def plot_over_one_curve():
    """在一张表中画多个曲线"""
    x = np.linspace(-np.pi * 2, np.pi * 2, 100)
    plt.figure(1, dpi=50)

    for i in range(1, 5):
        plt.plot(x, np.sin(x / i))

    plt.show()

def plot_hist():
    """绘制直方图"""
    plt.figure(1, dpi=50)
    data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
    plt.hist(data)  # 只要传入数据，直方图就会统计数据出现的次数
    plt.show()

def plot_scatter():
    """绘制散点图"""
    x = np.arange(1, 10)
    y = x * 2 + 1
    fig = plt.figure()
    # c = 'r'表示散点的颜色为红色，marker 表示指定散点的形状为圆
    plt.scatter(x, y, c='r', marker='o')
    plt.show()

def plot_pie():
    """绘制饼图"""
    data = [100, 500, 300]
    fig = plt.figure(dpi=80)
    plt.pie(data,   # 每个饼块的实际数据，如果大于1，会进行归一化，计算百分比
            explode=[0., 0., 0.1],      # 每个饼块里中心的距离
            colors=['y', 'r', 'g'],     # 每个饼块的颜色
            labels=['A part', 'B part', 'C part'],  # 每个饼块的标签
            labeldistance=1.1,          # 每个饼块标签到中心的距离
            autopct='%1.1f%%',          # 百分比的显示格式
            pctdistance=0.5,            # 百分比到中心的距离
            shadow=True,                # 每个饼块是否显示阴影
            startangle=0,               # 默认从x轴正半轴逆时针起
            radius=1)                   # 饼块的半径
    plt.show()

def plot_load_file():
    """加载文件并绘图"""
    data = np.loadtxt('data.txt', delimiter=',')
    # print(type(data))       # <class 'numpy.ndarray'>
    # print(data.shape)       # (21, 2)
    # ro表示每个数据在图表上打印的是红色的圆点
    plt.plot(data[:, 0], data[:, 1], 'ro')
    plt.show()


if __name__ == '__main__':
    # simple_test()
    # simple_test2()
    # simple_test3()
    # simple_test4()
    # plot_sin()
    # plot_sca()
    # plot_over_one_curve()
    # plot_hist()
    # plot_scatter()
    # plot_pie()
    plot_load_file()
