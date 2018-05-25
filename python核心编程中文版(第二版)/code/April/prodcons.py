# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = prodcons
@author = Liangjisheng
@create_time = 2018/4/10 0010 下午 18:58
"""
# 生产者，消费者问题
from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread


def writeQ(queue):
    print('producing object for Q...', queue.put('xxx', 1))
    print('size now', queue.qsize())


def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q... size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')


if __name__ == '__main__':
    main()
