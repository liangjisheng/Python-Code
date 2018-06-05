# -*- coding:utf-8 -*-
"""
@project = 0604-1
@file = operator_2
@author = Liangjisheng
@create_time = 2018/6/5 0005 下午 19:51
"""
import operator as op

# 原地操作符 即in-place操作,x += y 等同于x=iadd(x, y),
# 如果复制给其他变量比如z = iadd(x, y)等同与z = x; z += y
a, b = 3, 4
c = [1, 2]
d = ['a', 'b']
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
a = op.iadd(a, b)
print('a = operator.iadd(a, b) =>', a)
c = op.iconcat(c, d)
print('c = operator.iconcat(c, d) =>', c)
print()

# operator模块最特别的特性之一就是获取方法的概念,获取方法是运行时构造的一些可回调对象
# 用来获取对象的属性或序列的内容，获取方法在处理迭代器或生成器序列的时候特别有用
# 它们引入的开销会大大降低lambda或Python函数的开销

# 获取属性
class MyObj(object):
    def __init__(self, arg):
        super(MyObj, self).__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj(%s)' % str(self.arg)

objs = [MyObj(i) for i in range(5)]
print('objects:', objs)
g = op.attrgetter('arg')
vals = [g(i) for i in objs]
print('arg values:', vals)

objs.reverse()
print('reverse:', objs)
print('sorted:', sorted(objs, key=g))
print()

# 获取元素
list1 = [dict(val=-1 * i) for i in range(4)]
print('dictionaries:', list1)
g = op.itemgetter('val')
vals = [g(i) for i in list1]
print('values:', vals)
print('sorted:', sorted(list1, key=g))
print()

list2 = [(i, i * -2) for i in range(4)]
print('tuples:', list2)
# 定义函数g，获取对象的第1个域的值
g = op.itemgetter(1)
vals = [g(i) for i in list2]
print('values:', vals)
print('sorted:', sorted(list2, key=g))
