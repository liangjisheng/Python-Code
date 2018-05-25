# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = closure——1
@author = Liangjisheng
@create_time = 2018/3/31 0031 下午 12:04
"""


def foo():
    m = 3
    n = 4

    def bar():
        a = 5
        return m + n + a
    return bar


f = foo()
# bar()局部作用域中可以直接访问foo局部作用域中定义的m,n变量，
# 这种内部函数可以使用外部函数变量的行为就叫闭包
print(f())

# code object是python代码经过编译后的对象。它用来存储一些与代码有关的信息以及bytecode
import dis
code_obj = compile('sum([1, 2, 3])', "", 'single')
exec(code_obj)
# 使用dis查看字节码
dis.dis(code_obj)
print(f.__closure__)
