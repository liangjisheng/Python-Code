
# str()：函数返回一个用户易读的表达形式
# repr():产生一个解释器易读的表达形式

s = "Hello, Runoob";
print(str(s));
print(repr(s));
print(str(1/7));
# repr()可以转义字符串中的特殊字符
print(repr("hello, runoob\n"));
# repr()的参数可以是python的任何对象
print(repr((100, 200, ("test", "asdf"))));
print();

# 输出平方和立方
for x in range(1, 11):
	print(repr(x).rjust(2), repr(x * x).rjust(3), end = " ");
	print(repr(x * x * x).rjust(4));
	
for x in range(1, 11):
	print("{0:2d}{1:4d}{2:5d}".format(x, x * x, x * x * x));
	
print("{0} and {1}".format("google", "runoob"));
print("{1} and {0}".format("google", "runoob"));

print("{name}网址：{site}".format(name = "test", site = "www.baidu.com"));

str = input("请输入:");
print("你输入的内容是: ", str);

input();