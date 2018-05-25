
# 可以按下面的思路减少循环次数：
# 1.当最小值为最大公约数时，直接返回
# 2.当最小指不为最大公约数时，最大公约数不会大于最小值的1/2
# 3.求最大公约数理应从大到小循环递减求最大

def gcd(a, b):
	if b > a:
		a, b = b, a;	# b为最小值
	if a % b == 0:
		return b;
	
	# 倒序求最大公约数更合理
	for i in range(b // 2 + 1, 1, -1):
		if b % i == 0 and a % i == 0:
			return i;
		
	return 0;
	
a = int(input("Input a: "));
b = int(input("Input b: "));
print(gcd(a, b));

# 辗转相除法求最大公约数
def gcd1(x, y): # very fast
	return x if y == 0 else gcd1(y, x%y);

print(gcd1(378, 5940));
print(gcd1(5940, 378));