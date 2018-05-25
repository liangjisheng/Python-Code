# -*- coding:utf-8 -*-
"""
@project = 0330-1
@file = metaclasses_1
@author = Liangjisheng
@create_time = 2018/3/30 0030 下午 20:07
"""

# 元类是一个类，它的实例是其他的类


class C(object):
    pass


class CC:
    pass


print(type(C))
print(type(CC))
print(dir(C))
c = C()
print(C.__dict__)
print(C.__dir__)
print(c.__dict__)
print(c.__dir__)
print(c.__dir__())
# 这行代码和上面的一行代码其实是一样的，调用同样的方法
print(C.__dir__(c))
