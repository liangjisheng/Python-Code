# -*- coding:utf-8 -*-
"""
@project = 0520-1
@file = dict_1
@author = Liangjisheng
@create_time = 2018/5/20 0020 上午 8:53
"""
stu = {'num1': 'Tom', 'num2': 'Lucy', 'num3': 'Sam'}
print(stu)
# stu.clear()
# print(stu)
stu2 = stu.copy()
print(stu2)

# fromkeys(指定一个列表，把列表中的值作为字典的key,生成一个字典)
name = ['tom', 'lucy', 'sam']
print(dict.fromkeys(name))
print(dict.fromkeys(name, 25))
print(stu.get('num2'))
print(stu.keys())
print(stu.values())
print(stu.items())

name2 = stu.pop('num2')
print(name2, stu)

# popitem(随机获取某个键值对，并在字典中删除)
stu.update([('num2', 'Lucy')])
name = stu.popitem()
print(name, stu)
stu.update({'num2': 'Lucy'})
print(stu)
# setdefault(获取指定key的value，如果key不存在，则创建)
name = stu.setdefault('num4')
print(name, stu)
