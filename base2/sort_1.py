# -*- coding:utf-8 -*-
"""
@project = 0702-1
@file = sort_1
@author = Liangjisheng
@create_time = 2018/7/2 0002 下午 20:27
"""
import numpy as np

np.random.seed(42)
complex_numbers = np.random.random(5) + 1j * np.random.random(5)
print(complex_numbers)
print('sorted\n', np.sort_complex(complex_numbers))
print()

a = np.array([2, 4, 8])
print(np.argmax(a))     # 返回数组中最大值对应的下标
b = np.array([np.nan, 2, 4])
print(np.nanargmax(b))  # 与np.argmax功能相同,但忽略nan值
# argmin和nanargmin类似
print(np.argwhere(a <= 4))      # 根据条件搜索非0元素，并分组返回对应的下标
print()

# searchsorted函数为指定的插入值返回一个在有序数组中的索引位置，从这个位置插入可
# 以保持数组的有序性
a = np.arange(5)
indices = np.searchsorted(a, [-2, 7])
print('indices', indices)
print('The full array', np.insert(a, indices, [-2, 7]))
print()

# extract函数可以根据某个条件从数组中抽取元素
a = np.arange(7)
condition = (a % 2) == 0
print('even numbers', np.extract(condition, a))
print('non zero', np.nonzero(a))       # nonzero函数抽取数组中非0元素
