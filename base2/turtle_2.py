# -*- coding:utf-8 -*-
"""
@project = 0715-1
@file = turtle_2
@author = Liangjisheng
@create_time = 2018/7/16 0016 上午 10:55
"""
import turtle as tt

if __name__ == '__main__':
    tt.color('red', 'yellow')
    tt.begin_fill()
    while True:
        tt.forward(200)
        tt.left(170)
        if abs(tt.pos()) < 1:
            break
    tt.end_fill()
    tt.done()
