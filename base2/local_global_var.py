# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = local_global_var
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 17:56
"""
# 全局和局部变量
num = 9

def f1():
    num = 20

def f2():
    print(num)

def f3():
    global num
    num = 20


if __name__ == '__main__':
    f2()    # 9
    f1()    # 在f1中并没有改变全局变量num的值
    f2()    # 9

    # num不是个全局变量，所以每个函数都得到了自己的num拷贝，
    # 如果你想修改num，则必须用global关键字声明
    f3()
    f2()    # 20
