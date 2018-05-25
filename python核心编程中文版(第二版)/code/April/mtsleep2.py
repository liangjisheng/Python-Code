# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = mtsleep2
@author = Liangjisheng
@create_time = 2018/4/9 0009 下午 19:55
"""
import _thread
from time import sleep, ctime

loops = [2, 1]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()  # 释放锁


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()      # 锁住锁
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        # 判断锁是否被锁住，如果锁住返回True，否则返回False
        while locks[i].locked():
            pass

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
