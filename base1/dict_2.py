
# 同时遍历两个或更多序列，可以使用zip组合
questions = ["name", "quest", "favorite color"];
answers = ["lancelot", "the holy grail", "blue"];

for q, a in zip(questions, answers):
	print("What is your {0}? It is {1}." .format(q, a));

# 反向遍历一个序列
for i in reversed(range(1, 10, 2)):
	print(i);
	
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f);
print();
	 
# 列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，
# 依次往右进一层，左边#第一条语句是最后一层
test1 = [x * y for x in range(1, 5) if x > 2 for y in range(1, 4) if y < 3];
print(test1);

# 上面的语句相当于下面
for x in range(1, 5):
	if x > 2:
		for y in range(1, 4):
			if (y < 3):
				print(x * y, end = " ");
		print();
print();
	
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]];
# 推导语句，应该先执行最右侧的 for，但是左侧的for用[]括起来，所以它的
# 优先级提高了，会被先执行
[[print(row[i]) for row in matrix] for i in range(4)];
input();