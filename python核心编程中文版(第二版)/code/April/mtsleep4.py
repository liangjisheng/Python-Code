# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = mtsleep4
@author = Liangjisheng
@create_time = 2018/4/9 0009 下午 20:24
"""
# 与传一个函数很相似的另一个方法是在创建线程的时候，传一个可调用的类的实例供线程启动
# 的时候执行——这是多线程编程的一个更为面向对象的方法。相对于一个或几个函数来说，由于类
# 对象里可以使用类的强大的功能，可以保存更多的信息，这种方法更为灵活
import threading
from time import sleep, ctime
loops = [2, 1]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        # 将对应元组中的元素分别赋值到对应的参数中
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
