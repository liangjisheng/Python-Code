# -*- coding:utf-8 -*-
"""
@project = 0612-1
@file = numpy_2
@author = Liangjisheng
@create_time = 2018/6/13 0013 下午 17:21
"""
import numpy as np

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
b = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype='str')
print(a)
print(b)

b = b.astype(int)   # 转换数据类型
print(b)

# (4, )shape有一个元素即为一维数组，数组中有4个元素
print(np.array([1, 2, 3, 4]).shape)

b.shape = 4, 3
print(b)
# 当某个轴的元素为-1时，将根据数组元素的个数自动计算该轴的长度
b.shape = 2, -1
print(b)

# 使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变
a = np.array((1, 2, 3, 4))
b = a.reshape((2, 2))
print(b)
print()

# The view method creates a new array object that looks at them same data.
# 浅复制
a = np.arange(12)
b = a.view()    # b是新创建出来的数组，但和a共享数据
print(b is a)   # False
print(b)
b.shape = 2, 6
print(a.shape)  # (12,)
print(b)
b[0, 4] = 1234
print(b)
print(a)
print()

# 深复制 The copy method makes a complete copy of the array and its data.
a = np.arange(12)
a.shape = 3, 4
a[1, 0] = 1234
c = a.copy()
print(c is a)
c[0, 0] = 9999  # 改变c元素的值，不会影响a的元素
print(c)
print(a)

# 查询维度
print(a.ndim)   # 2
# 查询元素个数
print(a.size)   # 12
