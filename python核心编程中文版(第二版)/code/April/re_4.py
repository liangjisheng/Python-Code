# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = re_4
@author = Liangjisheng
@create_time = 2018/4/5 0005 下午 18:56
"""
import re

# ^表示匹配开始，即匹配以The开头的字符串
m = re.search('^The', 'The end.')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search('^The', 'end. The')
if m is not None:
    print(m.group())
else:
    print('not match')

# \b在单词的边界匹配
m = re.search(r'\bthe', 'bite the dog')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search(r'\bthe', 'bitethe dog')
if m is not None:
    print(m.group())
else:
    print('not match')

# \B不在单词的边界匹配
m = re.search(r'\Bthe', 'bitethe dog')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search(r'\Bthe', 'bite the dog')
if m is not None:
    print(m.group())
else:
    print('not match')
print()

print(re.findall('car', 'car'))
print(re.findall('car', 'scary'))
print(re.findall('car', 'carry the barcardi to the car'))
print()

# sub,subn用来进行字符串的替换
print(re.sub('X', 'xxxx', 'attn: X\n\nDear X,\n'))
print(re.subn('X', 'xxxx', 'attn: X\n\nDear X,\n'))
print(re.sub('[ae]', 'X', 'abcdef'))
print(re.subn('[ae]', 'X', 'abcdef'))

print(re.split(':', 'str1:str2:str3'))
print()

m = re.match('\bblow', 'blow')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match('\\bblow', 'blow')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(r'\bblow', 'blow')
if m is not None:
    print(m.group())
else:
    print('not match')
