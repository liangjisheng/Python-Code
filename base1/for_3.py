
for letter in "Runoob" :
	if letter == "o" :
		pass;
		print("执行pass块");
	print("当前字母: ", letter);

print("Good Bye");

# 使用内置enumerate函数进行遍历
sequence = [12, 34, 34, 23, 45, 76, 89];
for i, j in enumerate(sequence) :
	print(i, j);
print();
	
sum = 0;
for i in range(0, 101) : 
	sum += i;
print(sum);
print();

i = 1;
while i <= 9 :
	j = 1;
	while j <= i:
		mut = j * i;
		print("%d*%d = %d"%(j, i, mut), end = " ");
		j += 1;
	print("");
	i += 1;
print();

for i in range(1 ,6) :
	for j in range(1, i + 1):
		print("*", end = " ");
	print();

# 如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
# 如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行
# pass只是为了防止语法错误
# pass就是一条空语句。在代码段中或定义函数的时候，如果没有内容，或者先不做
# 任何处理，直接跳过，就可以使用pass

input();