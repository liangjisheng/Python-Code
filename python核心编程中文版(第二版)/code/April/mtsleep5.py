# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = mtsleep5
@author = Liangjisheng
@create_time = 2018/4/10 0010 下午 18:39
"""
# 创建线程的另一种方法，从Thread派生出一个子类，创建一个这个子类的实例
import threading
from time import sleep, ctime
loops = (2, 1)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    # 重载run()
    def run(self):
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
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
