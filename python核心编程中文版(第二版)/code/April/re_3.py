# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = re_3
@author = Liangjisheng
@create_time = 2018/4/5 0005 下午 17:45
"""
import re

m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match('[cr][23][dp][o2]', 'c2do')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match('r2d2|c3po', 'c2do')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match('r2d2|c3po', 'r2d2')
if m is not None:
    print(m.group())
else:
    print('not match')

# 重复，特殊字符，和子组
# \w匹配字母或数字即[A-Z][a-z][0-9],+表示出现1次或多次
# ?表示出现0次或1次
patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print(m.group())
else:
    print('not match')

# *表示匹配0次或者多次
patt = '\w+@(\w+\.)*\w+\.com'
m = re.match(patt, 'nobody@www.xxx.yyy.zzz.com')
if m is not None:
    print(m.group())
else:
    print('not match')
print()

m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('not match')

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('not match')

# group()通常用来显示所有匹配部分，也可用来获取个别匹配的子组
# 可以用groups()方法获取一个包含所有匹配子组的元组
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
else:
    print('not match')
print()

m = re.match('ab', 'ab')
if m is not None:
    print(m.group())
    print(m.groups())
else:
    print('not match')

m = re.match('(ab)', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
else:
    print('not match')

m = re.match('(a)(b)', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
else:
    print('not match')
print()

m = re.match('(a(b))', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
else:
    print('not match')
