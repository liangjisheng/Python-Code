
# Fibonacci series: 斐波纳契数列，两个元素的总和确定了下一个数
a, b = 0, 1;
i = 0;
while i < 15 :
	print(b, end = ",");
	a, b = b, a + b;
	i += 1;
print();

num1 = 10;
num2 = 388;
num3 = 98;
print(num1, num2, num3, sep = "@");

def fab(n): # n是一个数字
	if n < 1:
		print("输入有误");
		return -1;
	if n == 1 or n == 2:
		return 1;
	else:
		return fab(n - 1) + fab(n - 2);

i = 1;
while i < 10: 
	print(fab(i), end = " ");
	i += 1;
print();
	
input("点击Enter退出");