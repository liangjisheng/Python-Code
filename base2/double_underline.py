# -*- coding:utf-8 -*-
"""
@project = 0523-2
@file = double_underline
@author = Liangjisheng
@create_time = 2018/5/23 0023 下午 17:03
"""
class Test(object):
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__bar = 23

t = Test()
# 在属性列表中并没有找到__bar,而是有一个名为_Test__bar的属性，
# 这就是Python解释器所做的名称修饰。它这样做是为了防止变量在子类中被重写
print(dir(t))

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__bar = 'overridden'

t2 = ExtendedTest()
# 覆盖了父类的属性
print(t2.foo)
print(t2._bar)

# 正如你可以看到__baz变成_ExtendedTest__baz以防止意外修改
print(dir(t2))
print(t2._ExtendedTest__bar)
# 但原来的_Test__baz还在
print(t2._Test__bar)

# 双下划线名称修饰也适用于方法名称, 名称修饰会影响在一个类的上下文中
# 以两个下划线字符（"dunders"）开头的所有名称
_MangleGlobal__mangled = 23
class MangleGlobal(object):
    def test(self):
        return __mangled

# 我声明了一个名为_MangledGlobal__mangled的全局变量。然后我在名为MangledGlobal的类的
# 上下文中访问变量。由于名称修饰，我能够在类的test()方法内，以__mangled来引用
# _MangledGlobal__mangled全局变量
print(MangleGlobal().test())    # 23


# 也许令人惊讶的是，如果一个名字同时以双下划线开始和结束，则不会应用名称修饰
# 由双下划线前缀和后缀包围的变量不会被Python解释器修改
# 但是，Python保留了有双前导和双末尾下划线的名称，用于特殊用途
# 这样的例子有，__init__对象构造函数，或__call__ --- 它使得一个对象可以被调用
class PrefixPostfixTest(object):
    def __init__(self):
        self.__bam__ = 42

print(PrefixPostfixTest().__bam__)      # 42
