# -*- coding:utf-8 -*-
"""
@project = 1
@file = twrapme
@author = Liangjisheng
@create_time = 2018/3/27 0027 下午 20:18
"""

# 类定义了任何内建类型，增加时间属性;get(), set(), 还有字符串的表示方法
# 并授权所有保留的属性，访问这些标准类型

from time import time, ctime


class TimedWrapMe(object):

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError("argument of 'c', 'm' or 'a' req'd")
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return repr(self.__data)

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, item):
        self.__atime = time()
        return getattr(self.__data, item)


# 包装一个没有属性的对象，下面包装一个整数


timeWrappedObj = TimedWrapMe(932)
print(timeWrappedObj.gettimestr('c'))   # 实例创建时间
print(timeWrappedObj.gettimestr('m'))
print(timeWrappedObj.gettimestr('a'))
print(timeWrappedObj)
print(timeWrappedObj.gettimestr('c'))
print(timeWrappedObj.gettimestr('m'))
print(timeWrappedObj.gettimestr('a'))

timeWrappedObj.set('time is up')
print(timeWrappedObj.gettimestr('m'))
print(timeWrappedObj)
print(timeWrappedObj.gettimestr('c'))
print(timeWrappedObj.gettimestr('m'))
print(timeWrappedObj.gettimestr('a'))
