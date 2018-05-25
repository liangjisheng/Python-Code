# -*- coding:utf-8 -*-
"""
@project = 0520-1
@file = defaultdict_2
@author = Liangjisheng
@create_time = 2018/5/20 0020 下午 15:54
"""
from collections import defaultdict
def default_factory():
    return 'default value'
d = defaultdict(default_factory, foo='bar')
print(d)
print(d['foo'])
print(d['foo1'])
print(d)
