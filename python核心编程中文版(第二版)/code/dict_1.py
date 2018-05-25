# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = dict_1
@author = Liangjisheng
@create_time = 2018/3/31 0031 下午 20:36
"""
import copy

dict1 = {'bob':21, 'tom':19, 'a':1, 'b':2}
print(dict1)
dict2 = copy.deepcopy(dict1)
print(dict2)
dict1['bob'] = 20
print(dict1)
print(dict2)


