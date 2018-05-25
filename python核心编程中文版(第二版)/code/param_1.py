# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = param_1
@author = Liangjisheng
@create_time = 2018/4/1 0001 上午 10:31
"""
# 默认参数必须指向不变对象


def add_end(L=[]):
    L.append('end')
    return L


print(add_end([1, 2, 3]))
print(add_end(['x', 'y']))
print(add_end())
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 所有再次调用add_end时会出现两个'end'
# 定义默认参数要牢记一点：默认参数必须指向不变对象
print(add_end())    # ['end', 'end']


def add_end_1(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end_1())  # ['end']
# 再次调用时，只有一个end
print(add_end_1())  # ['end']


# 在函数内部，参数numbers接受到的是一个tuple,可以传入0个或多个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc())
print(calc(1, 2, 3))

# 如果已经有一个list或者tuple, Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去
list1 = [1, 3, 5, 7]
print(calc(*list1))     # *list1表示把这个list的所有元素作为可变参数传进去


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('xxxx', 30)
person('bob', 35, city='beijing')
person('bob', 35, city='beijing', job='engineer')

dict1 = {'city': 'beijing', 'job': 'engineer'}
# **dict1表示把dict1这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是dict1的一份拷贝，对kw的改动不会影响到函数外的dict1
person('bob', 35, **dict1)


# 如果要限制关键字参数的名字，可以用命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person1(name, age, *, city, job):
    print(name, age, city, job)


person1('jack', 24, city='beijing', job='engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


person2('jack', 24, 1, 2, 3, city='beijing', job='engineer')


# 命名关键字参数可以有缺省值，从而简化调用
def person3(name, age, *args, city='beijing', job):
    print(name, age, args, city, job)


person3('jack', 24, 1, 2, 3, job='engineer')

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、
# 可变参数、命名关键字参数和关键字参数


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
