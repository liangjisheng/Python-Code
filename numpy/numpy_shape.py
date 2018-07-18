# -*- coding:utf-8 -*-
"""
@project = 0713-1
@file = numpy_shape
@author = Liangjisheng
@create_time = 2018/7/13 0013 下午 14:31
"""
import numpy as np

data_1d = np.array([0, 1, 2, 3])
data_2d = np.arange(6).reshape(2, 3)
# x, y, z对应的shape元组是从右往左数的
# 抽象座标轴顺序从左向右。指定哪个轴，就只在哪个轴向操作，其他轴不受影响
# axis0=2, axis1=3, axis2=4
data_3d = np.arange(24).reshape(2, 3, 4)

# 检查ndarray数据的维度和大小，用dim和shape
print('data_1d')
print(data_1d.ndim)
print(data_1d.shape)
print('data_2d')
# print(data_2d)
print(data_2d.ndim)
print(data_2d.shape)
print('data_3d')
# print(data_3d)
print(data_3d.ndim)
print(data_3d.shape)
print()

data = np.array(np.arange(12))
np.random.shuffle(data)
data = data.reshape(3, 4)
print(data)
print(np.sort(data, axis=0))    # 相当于对列进行排序
print(np.sort(data, axis=1))    # 相当于对行进行排序
print()

data = np.arange(24).reshape(2, 3, 4)
print(data)
print(np.sum(data, axis=0))     # 0轴被sum压扁,1轴2轴不变
print(np.sum(data, axis=1))     # 1轴被sum压扁,0轴2轴不变
# cumsum，cumprod 不缩减轴向，只在指定轴向操作
