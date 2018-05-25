# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = test_3n+1
@author = Liangjisheng
@create_time = 2018/4/3 0003 下午 20:52
"""

# 3n+1猜想
# 对任何一个自然数n，如果它是偶数，那么把它砍掉一半；如果它是奇数，
# 那么把(3n+1)砍掉一半。这样一直反复砍下去，最后一定在某一步得到n=1


n = int(input('enter a integer: '))
i = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n + 1) // 2
    i += 1

print(i)
