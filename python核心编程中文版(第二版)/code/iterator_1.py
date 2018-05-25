# -*- coding:utf-8 -*-
"""
@project = 0331-1
@file = iterator_1
@author = Liangjisheng
@create_time = 2018/3/31 0031 下午 16:38
"""
# 创建迭代器，为容器对象添加__iter__()和__next__()方法
# __iter__()返回迭代器对象本身self,__next__()则返回每次调用next()或迭代时的元素
# 内置函数iter()将可迭代对象转换为迭代器

ita = iter([1, 2, 3])
print(type(ita))
print(next(ita))
print(next(ita))
print(next(ita))
# 当没有元素可以进行迭代时，next()会抛出StopIteration异常
# print(next(ita))

ita = iter((1, 2, 3))
print(type(ita))
ita = iter('xxxxx')
print(type(ita))
print(next(ita))
ita = iter({1: '1', 2: '2', 3: '3'})
print(type(ita))
print()


# create iterator object
class Container:
    """iterator object"""
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __iter__(self):
        print('[log] I made this iterator!')
        return self

    def __next__(self):
        print('[log] Calling __next__ method!')
        if self.start < self.end:
            i = self.start
            self.start += 1
            return i
        else:
            raise StopIteration()


c = Container(0, 5)
# for循环内部已经处理了StopIteration()异常
for i in c:
    print(i)
print()


# 另一种生成迭代器的方法是使用生成器，通过yield语句快速生成迭代器，省略了复杂的
# __iter__()和__next__()方法
def container(start, end):
    while start < end:
        yield start
        start += 1


c1 = container(0, 5)
print(type(c1))     # <class 'generator'>
print(next(c1))
next(c1)
# print(next(c1))        # StopIteration
for i in c1:
    print(i)
print()

# yield语句可以让一个普通函数变成一个生成器，并且相应的__next__()方法返回的是yield后面的值
# 一种更直观的解释是：函数第一次调用会执行到yield暂停，并返回一个生成器，再次调用next()时
# 会返回yield后面的值，并执行到下一个yield停止


def gen():
    yield 5
    yield 'hello'
    yield 'world'
    yield 4


for i in gen():
    print(i)
