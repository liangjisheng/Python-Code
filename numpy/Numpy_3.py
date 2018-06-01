# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_3
@author = Liangjisheng
@create_time = 2018/5/24 0024 下午 14:03
"""
# http://reverland.org/python/2012/08/22/numpy
import numpy as np

B = np.arange(3)
print(B)
print(np.exp(B))
print(np.sqrt(B))
print(np.sqrt(4))
C = np.array([2., -1., 4.])
print(np.add(B, C))
print(np.arange(0, 6, 2))   # [0 2 4]
print()

a = np.arange(10) ** 3
print(a)
print(a[2])
print(a[2:5])
a[:6:2] = -1000
print(a)
print(a[::-1])
print()

# for i in a:
    # print(i ** (1 / 3.), end=' ')

# 多维数组可以每个轴有一个索引。这些索引由一个逗号分割的元组给出
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=np.int)
print(b)
print(b[2, 3])
print(b[0:5, 1])        # each row in the second column of b
print(b[:, 1])          # equivalent to the previous example
print(b[1:3, :])        # each column in the second and third row of b
# 当少于轴数的索引被提供时，确失的索引被认为是整个切片
print(b[-1])            # the last row. Equivalent to b[-1, :]
print()

c = np.array([
            [[0, 1, 2],
             [10, 12, 13]],

             [[100, 101, 102],
              [110, 112, 113]]
              ])
print(c.shape)
print(c[1, ...])        # same as c[1, :, :] or c[1]
print(c[..., 2])        # same as c[:, :, 2]

# 迭代多维数组是就第一个轴而言的
for row in b:
    print(row)

# 然而，如果一个人想对每个数组中元素进行运算，我们可以使用flat属性，该属性是数组元素的一个迭代器:
for element in b.flat:
    print(element, end=' ')
print()
