# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = iterator_1
@author = Liangjisheng
@create_time = 2018/4/2 0002 下午 21:05
"""

for index, value in enumerate(['first', 'second', 'third']):
    print(index, ":", value)

print('上面是list,下面是dict')

for index, value in enumerate({'first': 1, 'second': 2, 'third': 3}):
    print(index, ':', value)

for x, y, z in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
    print(x, y, z)


# 通过迭代器对象来访问可迭代对象
L = ['appleyk', 'f', 24, 'python3']
it = iter(L)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break


from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('', Iterable))
print(isinstance((), Iterable))
print(isinstance(100, Iterable))
# 可以被next()函数调用并不断返回下一个值的对象成为迭代器

