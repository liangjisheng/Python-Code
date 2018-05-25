# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = mtsleep3
@author = Liangjisheng
@create_time = 2018/4/9 0009 下午 20:13
"""
# 创建线程的的一种方法：创建threading模块里面的Thread实例，传递给它一个对象
import threading
from time import sleep, ctime
loops = [2, 1]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    # 生成线程对象，此时线程对象里存储的线程函数并没有运行
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    # start threads
    for i in nloops:
        threads[i].start()

    # wait for all threads to finish
    for i in nloops:
        # join(timeout=None)程序挂起，直到线程结束,如果给了 timeout，则最多阻塞 timeout 秒
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
