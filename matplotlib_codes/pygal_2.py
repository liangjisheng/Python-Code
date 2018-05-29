# -*- coding:utf-8 -*-
"""
@project = 0527-2
@file = pygal_2
@author = Liangjisheng
@create_time = 2018/5/29 0029 上午 9:21
"""
import pygal
from datetime import datetime, timedelta

def simple_pygal1():
    """简单线图"""
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

    line_chart.render_to_file('simple_pygal1.svg')

def simple_pygal2():
    """与简单线图内容相同，但是图形的X轴与Y轴对调，即原来的X轴移动到垂直方向"""
    line_chart = pygal.HorizontalLine()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    line_chart.range = [0, 100]
    line_chart.render_to_file('simple_pygal2.svg')

def simple_pygal3():
    """将绘图数据累加汇出，可以绘制累加的百分比图，
    下面的例子里同时还对数据进行了填充"""

    line_chart = pygal.StackedLine(fill=True)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    line_chart.render_to_file('simple_pygal3.svg')

def simple_pygal4():
    """绘制与时间有关的数据线图，其横坐标为时间序列"""

    date_chart = pygal.Line(x_label_rotation=20)
    date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'),
                              [datetime(2013, 1, 2), datetime(2013, 1, 12),
                               datetime(2013, 2, 2), datetime(2013, 2, 22)])
    date_chart.add('Visits', [300, 412, 823, 672])

    date_chart.render_to_file('simple_pygal4.svg')


if __name__ == '__main__':
    # simple_pygal1()
    # simple_pygal2()
    # simple_pygal3()
    simple_pygal4()
