# -*- coding:utf-8 -*-
"""
@project = 0406-1
@file = gendata
@author = Liangjisheng
@create_time = 2018/4/6 0006 上午 10:27
"""

from random import randint, choice
from string import ascii_lowercase
from sys import maxsize
from time import ctime
import re

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5, 10)):
    dtint = randint(0, maxsize-1)
    dtstr = ctime()

shorter = randint(4, 7)
em = ''
for j in range(shorter):
    em += choice(ascii_lowercase)

longer = randint(shorter, 12)
dn = ''
for j in range(longer):
    dn += choice(ascii_lowercase)

# print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer))
data = '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
print(data)
patt = '^Mon|^Tue|^Wed|^Thu|^Fri|^Sat|^Sun'
patt1 = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'

m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(patt1, data)
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
else:
    print('not match')
print()

# 以三个有字符或数字组成的字符做为开头
patt2 = '^\w{3}'
m = re.match(patt2, data)
if m is not None:
    print(m.group())
else:
    print('not match')

patt = '\d+-\d+-\d+'
m = re.search(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')

# 匹配全部字符串的正则表达式
patt = '.+\d+-\d+-\d+'
m = re.search(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')

# 正则表达式本身默认是贪心匹配的, 如果正则表达式模式中使用到通配字，
# 那它在按照从左到右的顺序求值时，会尽量“抓取”满足匹配的最长字符串
# 在我们上面的例子里，“.+”会从字符串的起始处抓取满足模式的最长字符
# 其中包括我们想得到的第一个整数字段的中的大部分,\d+只需一位数字就可以匹配
patt = '.+(\d+-\d+-\d+)'
m = re.search(patt, data)
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
else:
    print('not match')

# 解决方法是用非贪婪操作符?,这个操作符可以用在*,+,?的后面，它的作用是要求
# 正则表达式匹配的字符越少越好
patt = '.+?(\d+-\d+-\d+)'
m = re.search(patt, data)
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
else:
    print('not match')
