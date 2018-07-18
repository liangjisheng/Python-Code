# -*- coding:utf-8 -*-
"""
@project = 0702-1
@file = ufunc_1
@author = Liangjisheng
@create_time = 2018/7/2 0002 下午 19:06
"""
import numpy as np

def answer(a):
    # 使用zeros_like函数创建一个和a形状相同，并且元素全部为0的数组result
    result = np.zeros_like(a)
    result.flat = 42
    return result

# 使用frompyfunc创建通用函数。指定输入参数的个数为1，随后的1为输出参数的个数
# 其实通用函数并非真正的函数，而是能够表示函数的对象
ufunc = np.frompyfunc(answer, 1, 1)
print('The answer', ufunc(np.arange(4)))
print('The answer', ufunc(np.arange(4).reshape(2, 2)))
print()

a = np.arange(9)
print('reduce', np.add.reduce(a))
print('accumulate', np.add.accumulate(a))
print('outer', np.add.outer(np.arange(3), a))
print()

# 矩阵除法
a = np.array([2, 6, 5])
b = np.array([1, 2, 3])
print('divide', np.divide(a, b), np.divide(b, a))
print('true_divide', np.true_divide(a, b), np.true_divide(b, a))
print('floor divide', np.floor_divide(a, b), np.floor_divide(a, b))

c = 3.14 * b
print('floor divide', np.floor_divide(c, b), np.floor_divide(b, c))
print(a / b)
print(a // b)
