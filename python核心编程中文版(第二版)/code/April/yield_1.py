# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = yield_1
@author = Liangjisheng
@create_time = 2018/4/1 0001 下午 12:34
"""


def Fib():
    a, b= 0, 1
    print('循环即将开始')
    for i in range(2):
        a, b = b, a + b
        print('即将运行到第' + str(i + 1) + '次yield')
        yield b
        print('第' + str(i + 1) + '次yield运行结束')


a = Fib()       # 得到一个生成器对象
print(next(a))
print()
print(next(a))
print()
# print(next(a))

# 生成器也可以使用next()方法获取下一个元素，因此生成器也属于迭代器，使用for循环
a1 = Fib()
for item in a1:
    print(item)
print()


# 与next()等价的方式
a2 = Fib()
print(a2.__next__())
print(a2.__next__())
print()


# send
def func():
    i = 0
    while i < 5:
        item = yield i
        print(item)
        i += 1


f = func()
print(f.__next__())
# item = yield i 这句首先执行等号右边的，yield返回，此时，返回生成器一个对象，并且中断
# 在下次使用 f.__next__( )时候，并没有传内容进去，所以可以认为yield i
# 这整个赋值给item的为None,所以item打印出为None
print(f.__next__())
print()

# send（）可以看做next（）的增强版除了可以使用next（）功能
# 还能传入一个值到上次yield断开地方的整体表达式（这里传给是yield i）
print(f.send('python'))
# print(f.__next__())
print()

print(f.send('xxxx'))
# print(f.__next__())
print()


f1 = func()
# 第一次的时候不能调send()，传入一个正常的参数，必须传入None
# print(f1.send('xxxx'))
print(f1.send(None))
print(f1.send('xxxx'))
