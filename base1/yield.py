
# Python中，使用了yield的函数被称为生成器(generator),
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，
# 更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有
# 的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行
# 以下实例使用 yield 实现斐波那契数列：

import sys;
"""
def fibonacci(n) : # 生成器函数，斐波那契
	a, b, counter = 0, 1, 0;
	while True :
		if (counter > n):
			return ;
		yield a;
		a, b = b, a + b;
		counter += 1;
		
f = fibonacci(10);	# f是一个迭代器，由生成器返回

while True:
	try :
		print(next(f), end = " ");
	except StopIteration :
		print();
		sys.exit();
"""

"""
def fibonacci1(n) : # 生成器函数，斐波那契
	a, b, counter = 0, 1, 0;
	while True :
		if (counter > n):
			return ;
		yield a;
		a, b = b, a + b;
		print("%d, %d" %(a, b));
		counter += 1;
		
f1 = fibonacci1(10);	# f是一个迭代器，由生成器返回

while True:
	try :
		print(next(f1), end = " ");
	except StopIteration :
		print();
		sys.exit();
"""

def fibonacci1(n, w = 0) : # 生成器函数，斐波那契
	a, b, counter = 0, 1, 0;
	while True :
		if (counter > n):
			return ;
		#yield a;
		a, b = b, a + b;
		print("%d, %d" %(a, b));
		counter += 1;
		
f1 = fibonacci1(10, 0);	# f是一个迭代器，由生成器返回

"""
while True:
	try :
		print(next(f1), end = " ");
	except StopIteration :
		print();
		sys.exit();
"""
		
input();