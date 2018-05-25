# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_5
@author = Liangjisheng
@create_time = 2018/3/25 0025 下午 17:26
"""


class P(object):
    """P class"""
    def __init__(self):
        print('created an instance of', self.__class__.__name__)

    def foo(self):
        print('Hi, I am P-foo()')


class C(P):
    def foo(self):
        print('Hi, I am C-foo()')


p = P()
p.foo()
print(p.__class__)
print(P.__bases__)
print(P.__doc__)

c = C()
c.foo()
print(c.__class__)      # 显示类的全名:模块名.类名
print(C.__bases__)      # 元组形式列出了父类
print(C.__doc__)        # __doc__特殊属性不会从基类继承过来

P.foo(c)          # 调用被覆盖的父类方法，调用非绑定方法
C.foo(c)          # 调用子类的非绑定方法
