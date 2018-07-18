# -*- coding:utf-8 -*-
"""
@project = 0709-1
@file = pygame_1
@author = Liangjisheng
@create_time = 2018/7/9 0009 下午 16:45
"""
import pygame
import sys
from pygame.locals import *

# 我们将初始化Pygame，创建一块400 × 300像素大小的显示区域，
# 并将窗口标题设置为Hello World!
pygame.init()
# 创建Surface对象用于绘图
screen = pygame.display.set_mode((400, 300))
# 设置标题
pygame.display.set_caption('Hello, World!')

# 游戏通常会有一个主循环一直运行，直到退出事件的发生。在本例中，我们仅仅在坐标
# (100, 100)处设置一个Hello World文本标签，文本的字体大小为19，颜色为红色
while True:
    sysFont = pygame.font.SysFont('None', 19)
    # 文本
    rendered = sysFont.render('Hello World', 0, (255, 100, 100))
    # 在Surface对象上进行绘制
    screen.blit(rendered, (100, 100))

    # get()获取Event对象列表
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()   # 清理pygame使用的资源
            sys.exit()

    # 刷新屏幕上显示的内容
    pygame.display.update()
