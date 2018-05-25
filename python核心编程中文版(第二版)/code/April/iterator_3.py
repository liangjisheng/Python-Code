# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = iterator_3
@author = Liangjisheng
@create_time = 2018/4/3 0003 下午 19:31
"""


def add(s, x):
    return s + x


def gen():
    for i in range(4):
        yield i


base = gen()
for n in [1, 10]:
    print(n)
    base = (add(i, n) for i in base)

print(list(base))
print()

gen1 = gen()
gen1 = (add(i, 1) for i in gen1)
print(list(gen1))
gen1 = (add(i, 2) for i in gen1)
print(list(gen1))
