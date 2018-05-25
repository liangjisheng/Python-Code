# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = iterator_5
@author = Liangjisheng
@create_time = 2018/4/3 0003 下午 20:36
"""
# 利用迭代器实现简单的“单线程并行”吃包子（实际上还是串行）
import time


def consumer(name):
    print('[%s] prepare to eat baozi!' % name)
    while True:
        baozi = yield
        print('baozi [%s] is coming, ate by [%s]' % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()

    print('start'.center(30, '-'))
    for i in range(10):
        time.sleep(0.5)
        print('just one, half to half')
        c.send(i)
        c2.send(i)


producer('wt')
