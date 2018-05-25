# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = iterator_2
@author = Liangjisheng
@create_time = 2018/4/3 0003 下午 19:20
"""


def eater(name):
    print('%s ready to eat' % name)
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        print('%s start to eat %s' % (name, food))


g = eater('xxxx')
print(g)
next(g)         # 等同于g.send(None), 初始化，第一次调用，执行到yield停止
print(g.send('food1'))
print(g.send('food2'))
