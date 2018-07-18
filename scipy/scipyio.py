# -*- coding:utf-8 -*-
"""
@project = 0709-1
@file = scipyio
@author = Liangjisheng
@create_time = 2018/7/9 0009 下午 15:56
"""
import numpy as np
from scipy import io
from scipy import stats
import matplotlib.pyplot as plt

# 将numpy数组保存为.mat文件, 在MATLAB或Octave环境中使用
# a = np.arange(7)
# io.savemat('a.mat', {'array': a})

# 生成正态分布的随机数
generated = stats.norm.rvs(size=900)
# 用正态分布去拟合生成的数据，得到其均值和标准差
print('mean, std', stats.norm.fit(generated))
# 偏度检验, 该检验有两个返回值，其中第二个返回值为p-value，
# 即观察到的数据集服从正态分布的概率
print('Skewtest, pvalue', stats.skewtest(generated))
# 峰度检验
print('Kurtosistest, pvalue', stats.kurtosistest(generated))
# 正态性检验, 可以检查数据集服从正态分布的程度
print('Normaltest, pvalue', stats.normaltest(generated))

# 使用SciPy我们可以很方便地得到数据所在的区段中某一百分比处的数值
print('95 percentile', stats.scoreatpercentile(generated, 95))  # 0.95分位数
# 将前一步反过来，我们也可以从数值1出发找到对应的百分比
print('Percentile at 1', stats.percentileofscore(generated, 1))

plt.hist(generated)
plt.show()
