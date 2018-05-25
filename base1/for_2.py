
for letter in "Runoob" : 
	if letter == "o" : 
		continue;
	print("当前字母: ", letter);

var = 10;
while var > 0 : 
	var -= 1;
	if 5 == var :
		continue;
	print("当前变量: ", var);
print("Good Bye");

# 循环语句可以有else子句，它在穷尽列表(for循环)或条件为False(while循环)导致
# 循环终止时被执行，但循环被break终止时不执行
for n in range(2, 10) :
	for x in range(2, n) :
		if n % x == 0:
			print(n, "等于", x, "*", n // x);
			break;
	else : 
		print(n, "是质数");
		
# pass是空语句，是为了保持程序结构的完整性
# pass不做任何事情，一般用作占位语句
while True : 
	pass;		# 等待键盘中断(Ctrl + C)
	
# 最小的类
class MyEmptyClass: 
	pass;

input();