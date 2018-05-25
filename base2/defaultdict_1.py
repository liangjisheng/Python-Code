# -*- coding:utf-8 -*-
"""
@project = 0520-1
@file = defaultdict_1
@author = Liangjisheng
@create_time = 2018/5/20 0020 下午 15:20
"""
# 众所周知，在Python中如果访问字典中不存在的键，会引发KeyError异常
# 是有时候，字典中的每个键都存在默认值是非常方便的
from collections import defaultdict
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}
# 该例子统计strings中某个单词出现的次数，并在counts字典中作记录。单词每出现一次，
# 在counts相对应的键所存的值数字加1
for kw in strings:
    if kw not in counts:
        counts[kw] = 1
    else:
        counts[kw] += 1

print(counts)

# 使用dict.setdefault()方法来设置默认值
counts.clear()
for kw in strings:
    # setdefault设置当前键值，如果当前键存在，返回键所对应的值，如果不存在
    # 将键所对应的值设置为0，并返回
    counts.setdefault(kw, 0)
    counts[kw] += 1
print(counts)

# dict.setdefault()方法的返回值可以重写for循环中的代码，使其更加简洁
counts.clear()
for kw in strings:
    counts[kw] = counts.setdefault(kw, 0) + 1
print(counts)

# defaultdict类就好像是一个dict，但是它是使用一个类型来初始化的
dd = defaultdict(list)
print(dd)
# defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值
print(dd['foo'])
print(dd)
dd['bar'].append('quux')
print(dd)
print('something' in dd)
dd.get('something')
print(dd['something'])
print(dd)
print()

# defaultdict类除了接受类型名称作为初始化函数的参数之外，还可以使用任何不带参数的可调用函数，
# 到时该函数的返回结果作为默认值，这样使得默认值的取值更加灵活
def zero():
    return 0

dd1 = defaultdict(zero)
print(dd1)
print(dd1['foo'])
print(dd1)

# 通过查看__getitem__()方法访问一个不存在的键时(dict[key]这种形式实际上是
# __missing__()方法获取默认值，并将该键添加到字典中去
counts.clear()
counts = defaultdict(lambda: 0)
for s in strings:
    counts[s] += 1
print(counts)
