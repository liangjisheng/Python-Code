
# 内置函数

class C(object):
	@staticmethod
	def f():
		print("runoob");

C.f();		# 调用静态方法无序实例化
cobj = C();
cobj.f();	# 也可以实例化后调用

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示

print(bin(10));
print(bin(20));
print(bin(40));

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
x = 7;
print(eval("3 * x"));
print(eval("pow(2, 2)"));
print(eval("2 + 2"));
n = 81;
print(eval("n + 4"));
print(eval("7"));

# int()用于将一个字符串或数字转换为整数
# class int(x, base = 10)
print(int());
print(int(3));
print(int(3.6));
# # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
print(int("12", 16));
print(int("0xa", 16));
print(int("10", 8));

# str() 函数将对象转化为适于人阅读的形式
print(str("runoob"));
dict1 = {"runoob":"runoob.com", "google":"google.com"};
print(dict1);
print(str(dict1));

# bool()函数用于将给定参数转换为布尔类型，如果没有参数，返回False
print(bool());
print(bool(0));
print(bool(1));
print(bool(2));
# bool 是int的子类
print(issubclass(bool, int));