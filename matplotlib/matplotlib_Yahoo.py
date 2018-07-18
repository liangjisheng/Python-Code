# -*- coding:utf-8 -*-
"""
@project = 0705-1
@file = matplotlib_Yahoo
@author = Liangjisheng
@create_time = 2018/7/5 0005 下午 19:55
"""
# 使用matplotlib.finance包中的函数可以从雅虎财经频道
# (http://finance.yahoo.com/)下载股价数据,并绘制成K线图(candlestick)
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.finance import _candlestick
import sys
from datetime import date
import matplotlib.pyplot as plt

# 将当前日期减去一年作为起始日期
today = date.today()
start = (today.year - 1, today.month, today.day)

# 创建定位器(locator)，这些来自matplotlib.dates包中的对象可以在
# x轴上定位月份和日期
alldays = DayLocator()
months = MonthLocator()

# 创建一个日期格式化器(date formatter)以格式化x轴上的日期
# 该格式化将创建一个字符串，包含简写的月份和年份
month_formatter = DateFormatter('%b %Y')

symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]
# 从雅虎财经频道下载股价数据
quotes = quotes_historical_yahoo_ochl(symbol, start, today)

# 创建一个Matplotlib的figure对象——这是绘图组件的顶层容器
fig = plt.figure()
# 增加一个子图
ax = fig.add_subplot(111)

# 将x轴上的主定位器设置为月定位器。该定位器负责x轴上较粗的刻度
ax.xaxis.set_major_locator(months)
# 将x轴上的次定位器设置为日定位器。该定位器负责x轴上较细的刻度
ax.xaxis.set_minor_locator(alldays)
# 将x轴上的主格式化器设置为月格式化器。该格式化器负责x轴上较粗刻度的标签
ax.xaxis.set_major_formatter(month_formatter)

# matplotlib.finance包中的一个函数可以绘制K线图。这样，我们就可以使用获取的
# 股价数据来绘制K线图。我们可以指定K线图的矩形宽度，现在先使用默认值
_candlestick(ax, quotes)

# 将x轴上的标签格式化为日期。为了更好地适应x轴的长度，标签将被旋转
fig.autofmt_xdate()
plt.show()
