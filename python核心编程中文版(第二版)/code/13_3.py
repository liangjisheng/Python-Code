# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_3
@author = Liangjisheng
@create_time = 2018/3/24 0024 下午 13:23
"""

# python中没有提供任何内部机制来跟踪一个类有所少个实例被创建了，或者记录这些
# 实例是干什么的，如果需要这些功能，可以显示加入一些代码到类定义__init__()
# __del__()中。最好使用静态成员来记录实例的个数

class InstCt(object):
    count = 0   # count is class attr

    # 如果定义了构造器，它不应该返回任何对象，因为实例对象是自动在实例化后返回的
    def __init__(self):
        InstCt.count += 1

    def __del__(self):
        InstCt.count -= 1

    def howMany(self):
        return InstCt.count


a = InstCt()
b = InstCt()
print(a.howMany())
print(b.howMany())
print(dir(a))           # 显示实例属性
print(a.__dir__())      # 显示实例属性
print(a.__dict__)       # 字典中仅有实例属性，没有类属性或者特殊属性
print(vars(a))
print(a.__class__)
print(InstCt.__class__)

del b
print(a.howMany())
del a
print(InstCt.count)
print()

# 内建类型属性
x = 3 + 0.14j
print(x.__class__)
print(dir(x))

print([type(getattr(x, i)) for i in ('conjugate', 'imag', 'real')])
print(x.imag)
print(x.real)
print(x.conjugate())

# 下面这两句话不会输出任何结果
#print(x.__dict__)      # 这句话会导致进程结束
print(x.__dir__())
print()

a = 1
print(type(a))
print(a.__class__)
print(dir(a))
