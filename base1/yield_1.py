
# 什么情况下需要使用 yield？
# 一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的
# 计算还是逻辑上的读取格式化）并且这个list会很大（无论是固定很大还是随着
# 输入参数的增大而增大),这个时候，我们希望每次调用这个函数并使用迭代器进
# 行循环的时候一个一个的得到每个list元素而不是直接得到一个完整的list来节
# 省内存，这个时候 yield 就很有用

import sys;

# 将前max个斐波那契数存储到列表L中，当这个max很大的时候会非常占用内存
# 因为我们实际使用的是list的遍历结果，也就是list的迭代器，那么可以让这个
# 函数fab每次只返回一个迭代器：即一个计算结果，而不是一个完整的list
"""
def fab(max): 
	n, a, b = 0, 0, 1;
	L = [];
	while n < max :
		L.append(b);
		a, b = b, a + b;
		n = n + 1;
	return L;

# fab()先生成了一个1000个元素的list，然后在去遍历list
f = iter(fab(100));

while True: 
	try : 
		print(next(f), end = " ");
	except StopIteration :
		print();
		sys.exit();
"""


def fab(max): 
	n, a, b = 0, 0, 1;
	#L = [];
	while n < max :
		yield b;
		#L.append(b);
		a, b = b, a + b;
		n = n + 1;
	#return L;

# 调用fab函数,while中的每次循环都在yield处中断并返回一个结果，然后
# 在次调用的时候在恢复中断继续运行
for x in fab(100):
	print(x);


input();