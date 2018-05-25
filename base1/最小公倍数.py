
def lcm(x, y):
	if x > y:
		greater = x;
	else:	
		greater = y;
		
	while True:
		if greater % x == 0 and greater % y == 0:
			res = greater;
			break;
		greater += 1;
	
	return res;
	
num1 = int(input("输入第一个数字: "));
num2 = int(input("输入第二个数字: "));

print(num1, "和", num2, "的最小公倍数为: ", lcm(num1, num2));


# 可按一下思路减少循环次数
# 1.当最大值为最下公倍数时，返回最大值
# 2.当最大值不为最小公倍数时，最小公倍数为最大值的倍数
def lcm1(a, b):
	if b > a:
		a, b = b, a;	# a为最大值
	if a % b == 0:
		return a;
	
	mul = 2;	# 最小公倍数为最大值的倍数
	while a * mul % b != 0:
		mul += 1;
	return a * mul;
	
a = int(input("Input a: "));
b = int(input("Input b: "));
print("最大公倍数: ", lcm1(a, b));