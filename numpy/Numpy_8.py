# -*- coding:utf-8 -*-
"""
@project = 0524-1
@file = Numpy_8
@author = Liangjisheng
@create_time = 2018/5/25 0025 下午 16:28
"""
import numpy as np
import numpy.linalg as lina

# 关于矩阵类的简短介绍
A = np.matrix('1.0, 2.0; 3.0, 4.0')
print(A)
print(type(A))      # file where class is defined
print(A.T)          # transpose
X = np.matrix('5.0, 7.0')
print(X)
Y = X.T
print(Y)
print(A * Y)        # matrix multiplication
print(A.I)          # inverse
print(lina.solve(A, Y))     # solving linear equation
print()

# NumPy中数组和矩阵有些重要的区别。NumPy提供了两个基本的对象：一个N维数组对象和
# 一个通用函数对象。其它对象都是建构在它们之上的。特别的，矩阵是继承自NumPy数组
# 对象的二维数组对象
A = np.arange(12)
A.shape = 3, 4
M = np.mat(A.copy())
print(type(A))
print(type(M))
print(A)
print(M)
# NumPy切片数组不创建数据的副本;切片提供统一数据的视图
print(A[:])
print(A[:].shape)
print(M[:])
print(M[:].shape)

# 现在有些和Python索引不同的了：你可以同时使用逗号分割索引来沿着多个轴索引
# 对二维数组使用一个冒号产生一个一维数组，然而矩阵产生了一个二维矩阵
print(A[:, 1])
print(A[:, 1].shape)
print(M[:, 1])
print(M[:, 1].shape)
print()

# 对二维数组使用一个冒号产生一个一维数组，然而矩阵产生了一个二维矩阵
a = np.arange(30)
a.shape = 2, -1, 3      # -1 means "whatever is needed"
print(a.shape)
print(a)

# 我们如何用两个相同尺寸的行向量列表构建一个二维数组, 在NumPy中这个过程通过函数
# column_stack、dstack、hstack和vstack来完成，取决于你想要在那个维度上组合
x = np.arange(0, 10, 2)                     # x=([0,2,4,6,8])
y = np.arange(5)                          # y=([0,1,2,3,4])
m = np.vstack([x, y])                      # m=([[0,2,4,6,8],
                                           #     [0,1,2,3,4]])
xy = np.hstack([x, y])                     # xy =([0,2,4,6,8,0,1,2,3,4])
