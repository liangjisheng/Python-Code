
# 阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
# 例如1^3 + 5^3 + 3^3 = 153
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407

num = int(input("请输入一个数字: "));

sum = 0;
# 获取num这个数字的位数，将其转换为字符串，在求长度
n = len(str(num));

tmp = num;
while tmp > 0:
	digit = tmp % 10;
	sum += digit ** n;
	tmp //= 10;
	
if num == sum:
	print(num, "是阿姆斯特朗数");
else:
	print(num, "不是阿姆斯特朗数");