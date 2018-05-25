# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = with_2
@author = Liangjisheng
@create_time = 2018/4/5 0005 下午 12:08
"""
# with经常被用来做异常处理,在with后面的代码块抛出任何异常时，__exit__() 方法被执行


class Sample(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('type:', exc_type)
        print('val:', exc_val)
        print('trace:', exc_tb)

    def do_something(self):
        bar = 1/0
        return bar + 10


with Sample() as sample:
    sample.do_something()
