
# 质数,检测用户输入的数字是否为质数

num = int(input("请输入一个数字: "));

if num > 1 :
	for i in range(2, num):
		if num % i == 0:
			print(num, "不是质数");
			print(i, "乘以", num // i, "是", num);
			break;
	else:
		print(num, "是质数");
else:
	print(num, "不是质数");
	

# 如果上面用于判断的数很大的话，就会显得时间复杂度较高，
# 可以在循环中使用平方根

import math;

num1 = int(input("请输入一个数字: "));

if num1 > 1:
	# 找到其平方根，减少算法时间
	num1_sqrt = math.floor(num1 ** 0.5);
	for i in range(2, (num1_sqrt + 1)):
		# 将平方根加1是为了能娶到平方根那个值
		if num1 % i == 0:
			print(num1, "是合数");
			print(i, "乘以", num1 // i, "是", num1);
			break;
	else:
		print(num1, "是质数");
else:
	print(num, "既不是质数，也不是合数");
	
print();


# 输出1-100以内的质数
count = 0;
for i in range(1, 101):
	for j in range(1, i):
		if j == i // 2 and i % j == 1 or (i <= 3 and i != 1):
			if count == 4:
				print(i);
				count = 0;
			else:
				print(i, end = "\t");
				count += 1;
			break;
		if i % j == 0 and j != 1:
			break;