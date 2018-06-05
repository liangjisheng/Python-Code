# -*- coding:utf-8 -*-
"""
@project = 0604-1
@file = os_listdir
@author = Liangjisheng
@create_time = 2018/6/4 0004 下午 20:28
"""
import os

path = os.getcwd()
# print(os.getcwd())
print(path)
# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
# 这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中
dirs = os.listdir(path)
print(dirs)
