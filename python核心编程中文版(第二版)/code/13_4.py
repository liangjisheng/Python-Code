# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_4
@author = Liangjisheng
@create_time = 2018/3/24 0024 下午 15:02
"""


class C(object):
    version = 1.2       # 静态成员，类属性，不可变对象
    x = {2003: 'poe2'}  # 可变对象


c = C()
print(C.version)        # 通过类访问类属性
print(c.version)        # 通过实例访问类属性
# 只能通过类来更新类属性，如果使用实例来更新，则会创建一个实例属性，隐藏类属性
# 任何对实例属性的赋值都会创建一个实例属性(如果不存在的话)并且对其赋值
C.version += 0.1
print(C.version)
print(c.version)

# 这句话相当于c.version = c.version + 0.2,首先计算等号右边的表达式，查找
# c.version找到了类属性，值为1.3.然后赋值给c.version,此时实例属性中并没有
# c.version，所以创建实例属性，最后实例属性的值为1.5
c.version += 0.2
print(c.version)    # 1.5
print(C.version)    # 1.3

print(c.x)
print(C.x)
c.x[2004] = 'valid path'
print(c.x)
print(C.x)

#使用实例属性来试着修改类属性是很危险的。原因在于实例拥有它们
#自已的属性集，在 Python 中没有明确的方法来指示你想要修改同名的类属性，比如，没有 global
#关键字可以用来在一个函数中设置一个全局变量（来代替同名的局部变量）。修改类属性需要使用类
#名，而不是实例名
