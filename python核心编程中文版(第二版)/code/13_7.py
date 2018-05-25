# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_7
@author = Liangjisheng
@create_time = 2018/3/26 0026 下午 18:57
"""


class MyClass(object):
    foo = 100

    def __int__(self):
        self.aaa = 100

    # @property
    def __len__(self):
        return 100


myInst = MyClass()
print(hasattr(myInst, 'aaa'))
print(hasattr(myInst, 'foo'))
print(getattr(myInst, 'foo'))

print(getattr(myInst, 'bbb', 123))  # 第三个参数提供默认值，如果属性不存在的话
setattr(myInst, 'bar', 'my attr')
print(hasattr(myInst, 'bar'))
print(getattr(myInst, 'bar'))
print(dir(myInst))
delattr(myInst, 'bar')
print(dir(myInst))
print(myInst.__getattribute__('foo'))
print(dir(MyClass))
print()

print(MyClass.__mro__)  # mro是方法解释顺序，以元组的形式列出了属性被搜索时的顺序

print(myInst.__dict__)
print(vars(myInst))
myInst.a = 10
myInst.str1 = 'test'
print(myInst.__dict__)
print(vars(myInst))  # 对象参数必须有一个__dict__属性
print(dir(myInst))
print(dir(MyClass))
print(vars())  # 没有参数的话，将显示一个包含本地名称空间的属性键值对
print(dir())  # 本地名称空间的属性名以列表形式给出

if myInst:
    print('myInst is True')  # print
else:
    print('myInst is False')

print(myInst)
print(str(myInst))
print(repr(myInst))
print(len(myInst))
