# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = with_1
@author = Liangjisheng
@create_time = 2018/4/5 0005 下午 12:04
"""
# 紧跟with后面的语句被求值后，返回对象的 __enter__() 方法被调用，
# 这个方法的返回值将被赋值给as后面的变量。
# 当with后面的代码块全部被执行完之后，将调用前面返回对象的 __exit__()方法


class Sample(object):
    def __enter__(self):
        print('In __enter__()')
        return 'Foo'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In __exit__()')


def get_sample():
    return Sample()


with get_sample() as sample:
    print('sample:', sample)
