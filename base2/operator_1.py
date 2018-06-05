# -*- coding:utf-8 -*-
"""
@project = 0604-1
@file = operator_1
@author = Liangjisheng
@create_time = 2018/6/5 0005 下午 18:02
"""
import operator as op

a = [1, 2, 3]
b = a
print('a =', a)
print('b =', b)
print('operator.not_(a):', op.not_(a))
print('operator.truth(a):', op.truth(a))
print('operator.is_(a, b):', op.is_(a, b))
print('operator.is_not(a, b):', op.is_not(a, b))
print()

a = 3
b = 5
print('a =', a)
print('b =', b)
for func in (op.lt, op.le, op.eq, op.ne, op.ge, op.gt):
    print('{0}({1}, {2}):'.format(func.__name__, a, b), func(a, b))
print()

a, b, c, d = -1, 2, -3, 4
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
# abs返回值得绝对值，neg返回(-obj), pos返回(+obj)
print('operator.abs(a):', op.abs(a))
print('operator.neg(a):', op.neg(a))
print('operator.neg(b):', op.neg(b))
print('operator.pos(a):', op.pos(a))
print('operator.pos(b):', op.pos(b))
print()

a, b = -2, 5.0
print('a =', a)
print('b =', b)
print('operator.add(a, b):', op.add(a, b))
# print('operator.div(a, b):', op.div(a, b))
print('operator.floordiv(a, b):', op.floordiv(a, b))
print('operator.mod(a, b):', op.mod(a, b))
print('operator.mul(a, b):', op.mul(a, b))
print('operator.pow(a, b):', op.pow(a, b))
print('operator.sub(a, b):', op.sub(a, b))
print('operator.truediv(a, b):', op.truediv(a, b))
print()

a, b = 2, 6
print('a =', a)
print('b =', b)
print('operator.and_(a, b):', op.and_(a, b))
print('operator.invert(a, b):', op.invert(a))
print('operator.lshift(a, b):', op.lshift(a, b))
print('operator.or_(a, b):', op.or_(a, b))
print('operator.rshift(a, b):', op.rshift(a, b))
print('operator.xor(a, b):', op.xor(a, b))
print()
