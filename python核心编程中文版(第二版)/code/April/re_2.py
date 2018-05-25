# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = re_2
@author = Liangjisheng
@create_time = 2018/4/5 0005 下午 17:35
"""
import re
# .匹配任何单个字符(换行符\n除外)

anykey = '.end'

m = re.match(anykey, 'bend')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(anykey, 'end')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(anykey, '\nend')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search('.end', 'The end.')
if m is not None:
    print(m.group())
else:
    print('not search')

# 匹配.需要加上\转义字符
patt314 = '3.14'
pi_patt = '3\.14'

m = re.match(pi_patt, '3.14')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(pi_patt, '3014')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(patt314, '3.14')
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.match(patt314, '3014')
if m is not None:
    print(m.group())
else:
    print('not match')
