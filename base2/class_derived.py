# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = class_derived
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 17:38
"""
class A(object):
    def show(self):
        print('base show')

class B(A):
    def show(self):
        super().show()
        print('derived show')


if __name__ == '__main__':
    objA = A()
    print(objA.__class__)
    objA.show()

    objB = B()
    print(objB.__class__)
    objB.show()

    # TypeError: __class__ must be set to a class, not 'NoneType' object
    # objB.__class__ = objA.show()
