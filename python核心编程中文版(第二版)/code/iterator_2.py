# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = iterator_2
@author = Liangjisheng
@create_time = 2018/3/31 0031 下午 18:07
"""
# 实现了__iter__()方法的对象是一个可迭代对象，__iter__()返回自身
# 实现了__next__()方法的对象是一个迭代器，用于迭代遍历一个可迭代对象
from itertools import islice


class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


# Fib既是一个可迭代对象(因为它实现了__iter__方法),又是一个迭代器(实现了__next__())
f = Fib()
print(list(islice(f, 0, 10)))
for i in range(10):
    print(next(f))
print()


# 生成器起始是一种特殊迭代器，只需要一个yield关键字，用生成器实现斐波那契数列
# 生成器是一种特殊的迭代器，它的返回值不是通过return而是用yield
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


# fib()是一个普通的函数，函数的返回值是一个生成器对象，当执行f1 = fib()时，fib()返回
# 的是一个生成器对象，此时函数体中的代码并不会执行，只有显示或隐式地调用next的时候才
# 会真正执行里面的代码
f1 = fib()
print(list(islice(f1, 0, 10)))


# 生成器表达式，看起来像列表推导式，但是它返回的是一个生成器对象而不是列表对象
a = (x * x for x in range(10))
print(a)
print(list(a))
