
#/usr/bin/env python

from random import randint;

def odd(n): return n % 2;

allNums = [];
for eachNum in range(9):
	allNums.append(randint(1, 99));
print(filter(odd, allNums));

print(list(filter(odd, allNums)));

# 使用lambda表达式
print(list(filter(lambda n : n % 2, allNums)));

# 使用列表生成器
print([n for n in allNums if n % 2]);

print([n for n in [randint(1, 99) for i in range(9)] if n % 2]);
print();

print(map((lambda x : x + 2), [0, 1, 2, 3, 4, 5]));
print(list(map((lambda x : x + 2), [0, 1, 2, 3, 4, 5])));
print(list(map((lambda x : x ** 2), list(range(6)))));
print([x + 2 for x in range(6)]);
print([x ** 2 for x in range(6)]);
print();

print(list(map((lambda x, y : x + y), [1, 3, 5], [2, 4, 6])));
print(list(map((lambda x, y : (x + y, x - y)), [1, 3, 5], [2, 4, 6])));

# [(1, 2), (3, 4), (5, 6)]
print(map(None, [1, 3, 5], [2, 4, 6]));
print(zip([1, 3, 5], [2, 4, 6]));
print(list(zip([1, 3, 5], [2, 4, 6])));
print();

#reduce()等同于下面的语句
#reduce(func, [1, 2, 3]) = func(func(1, 2), 3);
from functools import reduce;
print('the total is:', reduce((lambda x, y : x + y), range(5)));