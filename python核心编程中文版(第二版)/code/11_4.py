
#!/usr/bin/env python
# 这个脚本用传入的转换函数简单讲一个序列的数转换为相同的类型
# func是对这个函数对象的引用，func()是对这个函数对象的调用

def convert(func, seq):
	"""convert sequence of numbers to same type"""
	return [func(eachNum) for eachNum in seq];
	
myseq = (123, 45.67, -6.2e8, 999999999);
print(convert(int, myseq));
print(convert(float, myseq));