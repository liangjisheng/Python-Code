# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = gen_1
@author = Liangjisheng
@create_time = 2018/4/3 0003 下午 20:24
"""

# 如果用小括号则a是一个生成器对象，等号右边叫生成器表达式，如果用中括号则a是一个列表，可迭代对象
a = (i for i in range(4))
print(type(a))
print(a)
for i in a:
    print(i)
print()

# 不会输出任何结果，a是一个生成器对象，上面的那个循环已经将a循环到末尾了
for i in a:
    print(i)


def count(n):
    print('counting')
    while n > 0:
        print('before yield')
        yield n     # 生成值 n
        print(n)
        n -= 1
        print('after yield')


# c是一个生成器对象，并不是一个函数对象
c = count(7)
print(type(c))
c.__next__()
print()
c.__next__()
c.__next__()
print()

for i in count(5):
    print(i)
print()


c1 = count(5)
while True:
    try:
        print(next(c1), end=' ')
    except StopIteration:
        print()
        break

