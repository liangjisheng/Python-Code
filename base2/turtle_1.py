# -*- coding:utf-8 -*-
"""
@project = 0715-1
@file = Turtle_1
@author = Liangjisheng
@create_time = 2018/7/16 0016 上午 10:52
"""
import turtle as tt


def nose(x, y):          # 鼻子
    tt.penup()          # 提起笔
    tt.goto(x, y)       # 定位
    tt.pendown()        # 落笔，开始画
    tt.setheading(-30)  # 将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    tt.begin_fill()     # 准备开始填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            tt.left(3)      # 向左转3度
            tt.forward(a)   # 向前走a的步长
        else:
            a = a - 0.08
            tt.left(3)
            tt.forward(a)

    tt.end_fill()      # 填充完成
    tt.penup()
    tt.setheading(90)
    tt.forward(25)
    tt.setheading(0)
    tt.forward(10)
    tt.pendown()
    tt.pencolor(255, 155, 192)  # 画笔颜色
    tt.setheading(10)
    tt.begin_fill()
    tt.circle(5)
    tt.color(160, 82, 45)   # 返回或设置pencolor和fillcolor
    tt.end_fill()
    tt.penup()
    tt.setheading(0)
    tt.forward(20)
    tt.pendown()
    tt.pencolor(255, 155, 192)
    tt.setheading(10)
    tt.begin_fill()
    tt.circle(5)
    tt.color(160, 82, 45)
    tt.end_fill()


def head(x, y):      #   头
    tt.color((255, 155, 192), "pink")
    tt.penup()
    tt.goto(x, y)
    tt.setheading(0)
    tt.pendown()
    tt.begin_fill()
    tt.setheading(180)
    tt.circle(300, -30)
    tt.circle(100, -60)
    tt.circle(80, -100)
    tt.circle(150, -20)
    tt.circle(60, -95)
    tt.setheading(161)
    tt.circle(-300, 15)
    tt.penup()
    tt.goto(-100, 100)
    tt.pendown()
    tt.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            tt.lt(3)     # 向左转3度
            tt.fd(a)     # 向前走a的步长
        else:
            a = a - 0.08
            tt.lt(3)
            tt.fd(a)
    tt.end_fill()


def ears(x, y):      #耳朵
    tt.color((255, 155, 192), "pink")
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.begin_fill()
    tt.setheading(100)
    tt.circle(-50, 50)
    tt.circle(-10, 120)
    tt.circle(-50, 54)
    tt.end_fill()
    tt.penup()
    tt.setheading(90)
    tt.forward(-12)
    tt.setheading(0)
    tt.forward(30)
    tt.pendown()
    tt.begin_fill()
    tt.setheading(100)
    tt.circle(-50, 50)
    tt.circle(-10, 120)
    tt.circle(-50, 56)
    tt.end_fill()


def eyes(x, y):                      # 眼睛
    tt.color((255, 155, 192), "white")
    tt.penup()
    tt.setheading(90)
    tt.forward(-20)
    tt.setheading(0)
    tt.forward(-95)
    tt.pendown()
    tt.begin_fill()
    tt.circle(15)
    tt.end_fill()
    tt.color("black")
    tt.penup()
    tt.setheading(90)
    tt.forward(12)
    tt.setheading(0)
    tt.forward(-3)
    tt.pendown()
    tt.begin_fill()
    tt.circle(3)
    tt.end_fill()
    tt.color((255, 155, 192), "white")
    tt.penup()
    tt.seth(90)
    tt.forward(-25)
    tt.seth(0)
    tt.forward(40)
    tt.pendown()
    tt.begin_fill()
    tt.circle(15)
    tt.end_fill()
    tt.color("black")
    tt.penup()
    tt.setheading(90)
    tt.forward(12)
    tt.setheading(0)
    tt.forward(-3)
    tt.pendown()
    tt.begin_fill()
    tt.circle(3)
    tt.end_fill()


def cheek(x, y):        # 腮
    tt.color((255, 155, 192))
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.setheading(0)
    tt.begin_fill()
    tt.circle(30)
    tt.end_fill()


def mouth(x, y):         # 嘴
    tt.color(239, 69, 19)
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.setheading(-80)
    tt.circle(30, 40)
    tt.circle(40, 80)


def setting():          # 参数设置
    tt.pensize(4)
    tt.hideturtle()        # 使乌龟无形（隐藏）
    tt.colormode(255)      # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    tt.color((255, 155, 192), "pink")
    tt.setup(840, 500)
    tt.speed(10)


def main():
    setting()               # 画布、画笔设置
    nose(-100, 100)         # 鼻子
    head(-69, 167)          # 头
    ears(0, 160)            # 耳朵
    eyes(0, 140)            # 眼睛
    cheek(80, 10)           # 腮
    mouth(-20, 30)          # 嘴
    tt.done()


if __name__ == '__main__':
    main()
