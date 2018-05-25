# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = onethr
@author = Liangjisheng
@create_time = 2018/4/9 0009 下午 19:34
"""
# 单线程中顺序执行两个循环
from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(2)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop1 at:', ctime())
    sleep(1)
    print('loop 1 done at:', ctime())


def main():
    print('starting at:', ctime())
    loop0()
    loop1()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
