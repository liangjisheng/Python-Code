# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_2
@author = Liangjisheng
@create_time = 2018/3/24 0024 上午 11:57
"""

class MyClass(object):
    """MyClass class definition"""
    myVersion = '1.1'   # 静态数据
    def showMyVersion(self):
        print(MyClass.myVersion)

print(dir(MyClass))         # 查看类的属性
print(MyClass.__class__)    # 类的类型
print(MyClass.__dict__)     # 查看类的属性，以字典形式返回
print(MyClass.__module__)   # 类定义所在的模块,类名完全由模块名所限定，全名为__main__.MyClass
print(vars(MyClass))        # 返回类的__dict__属性的内容
print(MyClass.__name__)     # 类名
print(MyClass.__doc__)      # 文档字符串
print(MyClass.__bases__)    # 类的所有父类构成的元组
mc = MyClass()
print(type(mc))
print(type(MyClass))
print()

stype  = type('What is your quest')     # stype是一个类型对象
print(stype)                # <class 'str'>
print(stype.__name__)       # str
print(type(stype))
print(type(int))
print(type(float))
print((type(complex)))
print(type(str))
print(type(3.14159265))     # <class 'float'>
print(type(3.14159265).__name__)    # float
print(type(0))

# python2.2版本之前，使用经典类，此时类是类对象，实例是实例对象，两个对象类型
# 之间没有任何关系，除了实例的__class__属性引用了被实例化以得到该实例的类
# 2.2版本之后，当定义一个类后，就创建了一个新的类型
