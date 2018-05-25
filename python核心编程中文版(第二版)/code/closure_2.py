# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = closure_2
@author = Liangjisheng
@create_time = 2018/3/31 0031 下午 15:12
"""
# https://www.cnblogs.com/JohnABC/p/4076855.html
# 闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)
# 函数只是一段可执行代码，编译后就“固化”了，每个函数在内存中只有一份实例，
# 得到函数的入口点便可以执行函数了。在函数式编程语言中，函 数是一等公民
# （First class value：第一类对象，我们不需要像命令式语言中那样借助函数指针，委托操作函数），
# 函数可以作为另一个函数的参数或返回值，可以赋给一个变量。
# 函数可 以嵌套定义，即在一个函数内部可以定义另一个函数，
# 有了嵌套函数这种结构，便会产生闭包问题


def ExFunc(n):
    mysum = n

    def InsFunc():
        return mysum + 1
    return InsFunc


# 每次调用ExFunc函数后都将生成并保存一个新的局部变量sum。其实这里ExFunc函数返回的就是闭包
myFunc = ExFunc(10)
print(myFunc.__name__)
print(type(myFunc))
print(myFunc())
myFunc1 = ExFunc(20)
print(myFunc1.__name__)
print(type(myFunc1))
print(myFunc1())
print()

# 按照命令式语言的规则，ExFunc函数只是返回了内嵌函数InsFunc的地址，
# 在执行InsFunc函数时将会由于在其作用域内找不到sum变量而出错。
# 而在函数式语言中，当内嵌函数体内引用到体外的变量时，将会把定义时涉及到的
# 引用环境和函数体打包成一个整体（闭包）返回。现在给出引用环境的定义就 容易理解了：
# 引用环境是指在程序执行中的某个点所有处于活跃状态的约束
# （一个变量的名字和其所代表的对象之间的联系）所组成的集合。
# 闭包的使用和正常的函 数调用没有区别。由于闭包把函数和运行时的引用环境
# 打包成为一个新的整体，所以就解决了函数编程中的嵌套所引发的问题。
# 如上述代码段中，当每次调用ExFunc函数 时都将返回一个新的闭包实例，这些实例之间是隔离的，
# 分别包含调用时不同的引用环境现场。不同于函数，闭包在运行时可以有多个实例，
# 不同的引用环境和相同 的函数组合可以产生不同的实例


# 闭包中不能修改外部作用域的局部变量
def foo():
    m = 0

    def foo1():
        m = 1       # shadows name 'm' from outer scope
        print(m)

    print(m)
    foo1()
    print(m)


foo()
print()


# 另一个使用闭包的经典错误代码
def func():
    a = 1

    def func1():
        # nonlocal a
        a = a + 1
        return a
    return func1


# 下面这句话执行的时候，python会导入闭包函数体func1()来分析其局部变量，python指定所有在赋值
# 语句左边的变量都是局部变量，则在闭包func1中，a被认为是func1的局部变量，接下来在执行print(f1())
# 时，因为a被认为是局部变量，所以python会在func1()中找a，结果就是没找到，报错
# f1 = func()
# print(f1())

# python2.x版本可以这样解决
def func2():
    a = [2]

    def func2_1():
        a[0] = a[0] + 1
        return a[0]
    return func2_1


# 将a设定为一个容器
f2 = func2()
print(f2())


# python3.x版本可以这样解决,nonlocal a显示指定a不是闭包a的局部变量
def func3():
    a = 3

    def func3_1():
        nonlocal a
        a = a + 1
        return a
    return func3_1


f3 = func3()
print(f3())
