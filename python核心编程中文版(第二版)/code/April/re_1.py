# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = re_1
@author = Liangjisheng
@create_time = 2018/4/5 0005 下午 17:16
"""
import re

# match从一个字符串的开头开始匹配模式
m = re.match('foo', 'foo')
if m is not None:
    print(type(m))
    print(m.group())
    print(m.groups())
    print(m.start())
    print(m.end())
    print(m.endpos)

m = re.match('foo', 'bar')
if m is not None:
    print(m.groups())
else:
    print('not match')

m = re.match('foo', 'food on the table')
print(m.group())
print()

# search会检查参数字符串任意位置的地方给定正则表达式的匹配情况
# 如果搜索到成功的匹配，会返回一个匹配对象，否则返回None
m = re.match('foo', 'seafood')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search('foo', 'seafood')
if m is not None:
    print(m.group())
else:
    print('not search')
print()

bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(bt, 'blt')
if m is not None:
    print(m.group())
else:
    print('not match')
print()

m = re.match(bt, 'He bit me!')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search(bt, 'He bit me')
if m is not None:
    print(m.group())
else:
    print('not match')
print()
