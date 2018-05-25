
# classmethod修饰符对应的函数不需要实例化，不需要self参数，但第一个参数需要
# 是表示自身类的cls参数，可以来调用类的属性，类的方法，实例化对象

class A(object):
	bar = 1;
	def func1(self):
		print("foo");
	@classmethod
	def func2(cls):
		print("func2");
		print(cls.bar);
		cls().func1();		# 调用func1方法
		
A.func2();		# 不需要实例化

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
# 利用 * 号操作符，可以将元组解压为列表
a = [1, 2, 3];
b = [4, 5, 6];
c = [4, 5, 6, 7, 8];

zipped = zip(a, b);
print(zipped);			# 打包为元组的列表

print(zip(a, c));		# 元素个数与最短的列表一致
print(zip(*zipped));	# 与zip相反，可理解为解压，返回二维矩阵

# compile() 函数将一个字符串编译为字节代码
str = "for i in range(0, 10): print(i)";
str_c = compile(str, "", "exec");	# 编译为字节代码对象
print(str_c);
exec(str_c);

str = "3 * 4 + 5";
str_c = compile(str, "", "eval");
print(str_c);
print(eval(str_c));