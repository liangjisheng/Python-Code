# -*- coding:utf-8 -*-
"""
@project = 0702-1
@file = mod_1
@author = Liangjisheng
@create_time = 2018/7/2 0002 下午 20:14
"""
import numpy as np

a = np.arange(-4, 4)
# remainder函数逐个返回两个数组中元素相除后的余数。如果第二个数字为0，则直接返回0
# mod函数与remainder函数的功能完全一致
print('remainder', np.remainder(a, 2))
print('mod', np.mod(a, 2))
print(a % 2)

# fmod函数所得余数的正负由被除数决定，与除数的正负无关
print('fmod', np.fmod(a, 2))
print()
