
#/usr/bin/env python
# 偏函数应用(PFA),相当于C++里面的函数适配器

from operator import add, mul;
from functools import partial;

add1 = partial(add, 1);		# add1(x) = add(1, x)
mul100 = partial(mul, 100);	# mul100(x) = mul(100, x);

print(add1(10));
print(add1(1));
print(mul100(10));
print(mul100(500));

baseTwo = partial(int, base = 2);
baseTwo.__doc__ = 'Convert base 2 string to an int';
print(baseTwo('10010'));