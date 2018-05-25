# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = closure_3
@author = Liangjisheng
@create_time = 2018/3/31 0031 下午 15:48
"""

# 当循环结束以后，循环体中的临时变量i不会销毁，而是继续存在于执行环境中
for i in range(3):
    print(i)
print()

# 还有一个python的现象是，python的函数只有在执行时，才会去找函数体里的变量的值
flist = []
for i in range(3):
    def foo(x): print(x + i)
    flist.append(foo)

# 可能有些人认为这段代码的执行结果应该是2,3,4.但是实际的结果是4,4,4。这是因为当把
# 函数加入flist列表里时，python还没有给i赋值，只有当执行时，再去找i的值是什么，
# 这时在第一个for循环结束以后，i的值是2，所以以上代码的执行结果是4,4,4
for f in flist:
    f(2)
print()

# 解决方法如下
flist.clear()
for i in range(3):
    def foo(x, y=i): print(x + y)
    flist.append(foo)

# 2, 3, 4
for f in flist:
    f(2)

# 闭包主要是在函数式开发过程中使用


def hellocounter(name):
    count = [0]

    def counter():
        count[0] += 1
        print('hello', name, ',', str(count[0]), 'access!')
    return counter


# 我们可以把这个程序看做统计一个函数调用次数的函数
hello = hellocounter('xxxxx')
hello()
hello()
hello()

# 闭包返回一个元组里面存放了cell对象，即:闭包的环境相关的变量
print(hello.__closure__)
print(len(hello.__closure__))
for i in range(len(hello.__closure__)):
    print(hello.__closure__[i].cell_contents)
