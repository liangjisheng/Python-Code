# -*- coding:utf-8 -*-
"""
@project = 0406-1
@file = string_1
@author = Liangjisheng
@create_time = 2018/4/6 0006 上午 10:44
"""
import string
import random
# ascii_letters方法生成所有的字母，digits方法生成所有的数字
chars = string.ascii_letters + string.digits
print(chars)
print(string.ascii_lowercase)   # 小写字母
print(string.ascii_uppercase)


def rand_str(num, length=7):
    f = open('Activation_code.txt', 'w')
    for i in range(num):
        chars = string.ascii_letters + string.digits
        s = [random.choice(chars) for i in range(length)]
        f.write('{0}\n'.format(''.join(s)))
    f.close()


if __name__ == '__main__':
    rand_str(10)
