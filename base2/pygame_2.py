# -*- coding:utf-8 -*-
"""
@project = 0709-1
@file = pygame_2
@author = Liangjisheng
@create_time = 2018/7/9 0009 下午 17:09
"""
# Pygame提供Clock对象，用于控制每秒钟绘图的帧数。这可以保证动画与CPU的快慢无关
# 载入一个图像并使用NumPy定义一条沿屏幕的顺时针路径

import pygame
import sys
from pygame.locals import *
import numpy as np

pygame.init()
clock = pygame.time.Clock()     # 创建一个Pygame的Clock对象
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Animating Objects')
img = pygame.image.load('liangjisheng.jpg')     # 载入图像

# 我们将定义一些数组来储存动画中图片的位置坐标。既然对象可以被移动，那么应该有
# 四个方向——上、下、左、右。每一个方向上都有40个等距的步长。
# 我们将各方向上的值全部初始化为0
steps = np.linspace(20, 360, 40).astype(int)
right = np.zeros((2, len(steps)))
down = np.zeros((2, len(steps)))
left = np.zeros((2, len(steps)))
up = np.zeros((2, len(steps)))

right[0] = steps
right[1] = 20
down[0] = 360
down[1] = steps
left[0] = steps[::-1]
left[1] = 360
up[0] = 20
up[1] = steps[::-1]

pos = np.concatenate((right.T, down.T, left.T, up.T))
i = 0

while True:
    # 清屏
    screen.fill((255, 255, 255))
    if i >= len(pos):
        i = 0
    screen.blit(img, pos[i])
    i += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)
