# -*- coding:utf-8 -*-
"""
@project = 0330-1
@file = operator_1
@author = Liangjisheng
@create_time = 2018/3/30 0030 下午 20:54
"""

# operator模块提供了python中大多数标准操作符的函数版本, 某些情况下这种接口类型比标准操作符的硬编码方式更通用
from operator import add, sub, mul, floordiv


vec1 = [12, 24]
vec2 = [2, 3, 4]
OpVec = (add, sub, mul, floordiv)

for eachOp in OpVec:
    for i in vec1:
        for j in vec2:
            print('%s(%d, %d) = %d' % (eachOp.__name__, i, j, eachOp(i, j)))

