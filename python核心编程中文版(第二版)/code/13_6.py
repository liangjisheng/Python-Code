# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_6
@author = Liangjisheng
@create_time = 2018/3/25 0025 下午 18:09
"""

# 从标准类型派生，将浮点数精确到小数点后2位的类，不可变类型


class RoundFloat(float):
    def __new__(cls, val):
        return float.__new__(cls, round(val, 2))


class RoundFloat1(float):
    def __new__(cls, val):
        return super(RoundFloat1, cls).__new__(cls, round(val, 2))


print(RoundFloat(1.5955))
print(RoundFloat(1.5945))
print(RoundFloat(-1.9955))
print()

print(RoundFloat1(1.5955))
print(RoundFloat1(1.5945))
print(RoundFloat1(-1.9955))


# 简单的创建一个新的字典类型，它的keys()方法会自动排序结果


class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2), ('a', 1)))
print('By iterator:'.ljust(12), [key for key in d])     # keys以散列顺序输出
print('By keys():'.ljust(12), d.keys())                 # keys以字母排序方式输出
