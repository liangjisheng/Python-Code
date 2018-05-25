
# 阶乘

num = int(input("请输入一个数字: "));
factorial = 1;

if num < 0:
	print("抱歉，负数没有阶乘");
elif num == 0:
	print("0的阶乘为1");
else:
	for i in range(1, num + 1):
		factorial *= i;
	print("%d 的阶乘为 %d" %(num, factorial));
	
from functools import reduce;

# 计算num的阶乘
sum = reduce(lambda x, y: x * y, range(1, num + 1));
print("%d 的阶乘为 %d" %(num, sum));

import math;
if num < 0:
	print("负数没有阶乘");
else:
	print("{0} 的阶乘为 {1}".format(num, math.factorial(num)));