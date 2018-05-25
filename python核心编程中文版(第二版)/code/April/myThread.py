# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = myThread
@author = Liangjisheng
@create_time = 2018/4/10 0010 下午 19:01
"""
# 自定义线程类，继承自threading.Thread类
import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())
