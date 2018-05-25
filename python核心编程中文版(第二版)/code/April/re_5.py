# -*- coding:utf-8 -*-
"""
@project = 0406-1
@file = re_1
@author = Liangjisheng
@create_time = 2018/4/6 0006 上午 11:40
"""
import re
print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))

line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))
else:
    print('not match')
print()

pattern = re.compile(r'\d+')    # 至少匹配一个数字
m = pattern.match('one12twothree34four')
print(m)
# 从'e'的位置开始匹配，没有匹配
m = pattern.match('one12twothree34four', 2, 10)
print(m)
# 从'1'的位置开始匹配，正好匹配
m = pattern.match('one12twothree34four', 3, 10)
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print()

# 忽略大小写
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('Hello World Wide Web')
print(m)
print(m.group(0))   # 0可省略
print(m.span(0))    # 0可省略
print(m.group(1))
print(m.span(1))
print(m.group(2))
print(m.span(2))
print(m.groups())
# print(m.group(3))
