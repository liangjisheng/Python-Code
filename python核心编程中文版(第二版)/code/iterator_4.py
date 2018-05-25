# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = iterator_4
@author = Liangjisheng
@create_time = 2018/4/3 0003 下午 19:48
"""


class DataIter(object):
    def __init__(self, *args):
        self.data = list(args);
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind == len(self.data):
            raise StopIteration
        else:
            data = self.data[self.ind]
            self.ind += 1
            return data


# 迭代器是一次性消耗品，使用完了以后就空了
# DataIter既是一个迭代器又是一个可迭代对象，但只能迭代一遍，多调一次next()就会抛出StopIteration
d = DataIter(1, 2)
for x in d:
    print(x)

# 这个for循环不会输出任何结果，因为d这个迭代器已经到达了最后，每次都会抛出StopIteration的异常
for x in d:
    print(x)
print()

# print(d.__next__())   # 再调一次__next__()就会出错
# 下面将迭代器与可迭代对象分离，来解决上面只能迭代一次的情况


class Data(object):
    def __init__(self, *args):
        self.data = list(args)

    def __iter__(self):
        return DataIterator(self.data)


class DataIterator(object):
    def __init__(self, data):
        self.data = data
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind == len(self.data):
            raise StopIteration
        else:
            data = self.data[self.ind]
            self.ind += 1
            return data


if __name__ == '__main__':
    d = Data(1, 2, 3)
    for x in d:
        print(x)
    print()
    for x in d:
        print(x)
