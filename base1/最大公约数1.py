
def hcf(x, y):
	"""返回两个数的最大公约数"""
	if x > y:
		smaller = y;
	else:
		smaller = x;
	
	for i in range(1, smaller + 1):
		if x % i == 0 and y % i == 0:
			res = i;
	
	return res;
	
num1 = int(input("输入第一个数字: "));
num2 = int(input("输入第二个数字: "));

print(num1, "和", num2, "的最大公约数为: ", hcf(num1, num2));