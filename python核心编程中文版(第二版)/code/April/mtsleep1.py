# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = mtsleep1
@author = Liangjisheng
@create_time = 2018/4/9 0009 下午 19:48
"""
import _thread
from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(2)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(1)
    print('loop 1 done at:', ctime())


def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # _thread模块的主线程退出后，会强制结束所有的子线程，必需使得主线程还在运行，sleep(4)不能少
    sleep(4)
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
