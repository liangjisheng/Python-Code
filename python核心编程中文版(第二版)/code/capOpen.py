# -*- coding:utf-8 -*-
"""
@project = 1
@file = capOpen
@author = Liangjisheng
@create_time = 2018/3/27 0027 下午 20:45
"""

# 包装一个文件对象，在写模式中，字符串只有全部为大写是，才写入文件


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return repr(self.file)

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, item):
        return getattr(self.file, item)


f = CapOpen('test.txt', 'w')
f.write('delegation example\n')
f.write('faye is good\n')
f.write('at delegating\n')
f.close()
print(f)

f = CapOpen('test.txt', 'r')
for eachLine in f.readlines():
    print(eachLine)
