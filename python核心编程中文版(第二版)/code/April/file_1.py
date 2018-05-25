# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = file_1
@author = Liangjisheng
@create_time = 2018/4/1 0001 上午 9:13
"""

a = 'asdfasdfadsfadf'
utf8_a = a.encode()
print(a)
print(utf8_a)
print(type(a))
print(type(utf8_a))
print()

import random

print(random.random())                  # 用于生成0到1的随机浮点数 0<= n < 1.0
print(random.uniform(2, 3))             # 用于生成一个指定范围内的随机浮点数
print(random.randint(2, 4))             # 用于生成一个指定范围内的随机整数
print(random.randrange(10, 100, 2))     # 从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数
print()

# random.choice()从序列中获取一个随机元素
print(random.choice('asdfasdfa'))
print(random.choice(['a', 'b', 'c']))
print(random.choice(('a', 'b', 'c')))

# random.shuffle()将一个列表中的元素打乱
list1 = [1, 2, 3, 4, 5, 6]
random.shuffle(list1)
print(list1)
# random.sample()从指定序列中随机获取指定长度的序列
print(random.sample(list1, 3))
print(list1)
