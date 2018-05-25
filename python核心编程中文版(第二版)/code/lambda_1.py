# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = lambda_1
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 9:34
"""

# lambda表达式等同于匿名函数

func = lambda x: x + 1
print(func(1))

from functools import reduce

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x: x % 3 == 0, foo)))
print(list(map(lambda x: x * 2 + 10, foo)))
print(reduce(lambda x, y: x + y, foo))
print(sum(foo))

# python三目运算符
name = 'aaaa' if 1 == 1 else 'xxxx'
print(name)
name = 'aaaa' if 1 != 1 else 'xxxx'
print(name)
