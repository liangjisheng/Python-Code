# -*- coding:utf-8 -*-
"""
@project = 0520-1
@file = Counter_1
@author = Liangjisheng
@create_time = 2018/5/20 0020 上午 8:35
"""
# Counter（计数器）：用于追踪值的出现次数
# Counter类继承dict类，所以它能使用dict类里面的方法
import collections
obj = collections.Counter('aabbccc')
print(obj)
print(list(obj.elements()))
print(sorted(obj.elements()))
for elem in obj.elements():
    print(elem, end='', sep=' ')
print()

# most_common(指定一个参数n，列出前n个元素，不指定参数，则列出所有)
print(obj.most_common(2))
print(obj.most_common())

# items(从dict类中继承的方法)
print(obj.items())
for k, v in obj.items():
    print(k, v)

# update(增加元素)
obj.update(['a', 'd'])
print(obj)

# subtract(原来的元素减去新传入的元素)
obj.subtract(['a', 'b'])
print(obj)
