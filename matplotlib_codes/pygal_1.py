# -*- coding:utf-8 -*-
"""
@project = 0527-2
@file = pygal_1
@author = Liangjisheng
@create_time = 2018/5/27 0027 下午 19:19
"""
import random
import pygal

class Die(object):
    """创建一个骰子类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return random.randint(1, self.num_sides)


if __name__ == '__main__':
    die = Die()

    # 掷几次骰子 并将结果存储在一个列表中
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    frequencies = []
    # 分析结果
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    hist = pygal.Bar()
    hist.title = 'Result of rolling one d6 1000 times'
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of result"

    hist.add("D6", frequencies)
    hist.render_to_file("die_visual.svg")
