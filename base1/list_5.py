
# python的列表可以嵌套

# 3*4的矩阵列表
matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12]
		];
print(matrix);

# 将matrix转置
mat1 = [[row[i] for row in matrix] for i in range(4)];
print(mat1);

# 转置也可以使用下面的方法来实现
transposed = [];
for i in range(4):
	transposed.append([row[i] for row in matrix]);

print(transposed);

# 另一种实现方法
mat2 = [];
for i in range(4):
	# the following lines implement the nested listcomp
	mat2_row = [];
	for row in matrix:
		mat2_row.append(row[i])
	mat2.append(mat2_row);

print(mat2);
print();


# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用pop()
# 返回一个值不同。可以用del语句从列表中删除一个切割，或清空整个列表
# (我们以前介绍的方法是给该切割赋一个空列表)
a = [-1, 1, 66.25, 333, 333, 1234.5];
print(a);

del a[0];
print(a);

del a[2:4];
print(a);

del a[:];
print(a);

# 删除实体变量a
del a;

input();