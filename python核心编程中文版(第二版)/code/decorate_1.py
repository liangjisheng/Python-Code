# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = decorate_1
@author = Liangjisheng
@create_time = 2018/3/31 0031 上午 9:54
"""

# 装饰器其实就是一个函数，一个用来包装函数的函数，返回一个修改之后的函数
# 将其重新赋值原来的标识符，并永久丧失对原始对象的访问


def deco(func):
    print(func)
    return func


@deco
def foo():
    pass


# 此时foo()这样调用等于deco(foo)
foo()

# 简单的装饰器，检查函数有没有说明文档


def deco_funcNeedDoc(func):
    if func.__doc__ == None:
        print(func.__name__, "has no __doc__, it's a bad habit")
    else:
        print(func.__name__, ':', func.__doc__, '.')
    return func


@deco_funcNeedDoc
def f():
    print('f() do something')


@deco_funcNeedDoc
def g():
    """I have a __doc__"""
    print('g() do something')


f()
g()
