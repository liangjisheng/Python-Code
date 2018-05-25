# -*- coding:utf-8 -*-
"""
@project = 0511-1
@file = pathlib_1
@author = Liangjisheng
@create_time = 2018/5/11 0011 下午 18:46
"""
from pathlib import Path
# 创建Path对象
p = Path(r'D:\python\pycharm\projects\0511-1')
# 获取p的路径名称
print(p.name)
# 获取p目录下的所有文件, 返回一个迭代器，包含p下所有文件夹和文件
print(p.iterdir())
print(p.is_file())
print(p.is_dir())
print(Path.cwd())

tree_str = ''
def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '   |' * n + '-' * 4 + pathname.name + '\n'
        # print(tree_str)
    elif pathname.is_dir():
        tree_str += '   |' * n + '-' * 4 + str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


generate_tree(Path.cwd())
print(tree_str)
