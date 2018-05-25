
# 任何调用yield的函数都称为生成器，调用生成器函数创建一个对象，该对象通过
# 连续调用next()(python3里是__next()__)生成结果序列

def countdown(n):
	print("Counting down");
	while n > 0:
		yield n;	# 生成一个值
		n -= 1;

c = countdown(5);
print(c.__next__());
print(c.__next__());
print(c.__next__());
print(c.__next__());
print(c.__next__());
print();

for i in countdown(5):
	print(i);