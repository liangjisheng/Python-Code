
n = 100;
sum = 0;
counter = 1;

while counter <= n : 
	sum = sum + counter;
	counter += 1;

print("1到%d之和为: %d" %(n, sum));

# 使用Ctrl+C结束无限循环
while True : 
	num = int(input("输入一个数字"));
	print(num);
print("Good Bye");

input();