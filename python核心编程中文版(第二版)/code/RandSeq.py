# -*- coding:utf-8 -*-
"""
@project = 1
@file = RandSeq
@author = Liangjisheng
@create_time = 2018/3/26 0026 下午 20:45
"""

from random import choice


class RandSeq(object):
    """创建一个迭代器，__init__执行赋值操作，__iter__仅仅返回self, __next__
    得到迭代器中的连续的值，这个迭代器的唯一亮点是它没有终点，可以迭代无穷
    次，而一般的迭代器会引发StopIteration异常"""

    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def __next__(self):
        return choice(self.data)


# 程序会一直运行，不会停止
# for eachItem in RandSeq(('rock', 'paper', 'scissors')):
    # print(eachItem)


class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def __next__(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval


"""
a = AnyIter(range(10))
i = iter(a)
for j in range(1, 5):
    print(j, ':', i.__next__(j))
"""

"""
a = AnyIter(range(10))
i = iter(a)
print(i.__next__(14))
"""

a = AnyIter(range(10), True)
i = iter(a)
print(i.__next__(14))
