# -*- coding:utf-8 -*-
"""
@project = 0330-1
@file = dict_dir_1
@author = Liangjisheng
@create_time = 2018/3/30 0030 下午 21:11
"""

# dir()是一个函数，返回的是list，用来寻找一个对象的所有属性，包括__dict__中的属性
# __dict__是一个字典，键为属性名，值为属性值，__dict__是dir()的子集
# 许多内建类型没有__dict__属性，此时需要用dir()来列出对象的所有属性


class A(object):
    class_var = 1

    def __init__(self):
        self.name = 'xyz'
        self.age = 2

    @property
    def num(self):
        return self.age + 10


if __name__ == '__main__':
    a = A()
    # 实例的__dict__仅存储与该实例相关的实例属性，正因为实例的__dict__属性，每个实例的
    # 实例属性才会互不影响
    print(a.__dict__)
    # 类的__dict__存储所有实例共享的变量和函数，类的__dict__并不包含其父类的属性
    print(A.__dict__)

    a.level1 = 3
    a.fun = lambda x: x
    print(a.__dict__)
    print(A.__dict__)

    A.level2 = 4
    print(a.__dict__)
    print(A.__dict__)

    print()
    print(object.__dict__)

    # dir()是Python提供的一个API函数，dir()函数会自动寻找一个对象的所有属性(包括从父类中继承的属性)
    print(dir(a))
    print(dir(A))
