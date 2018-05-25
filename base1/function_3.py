
# any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，
# 如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True

# 列表list
print(any(["a", "b", "c", "d"]));	# True
print(any(["a", "b", "", "d"]));	# True
print(any([0, "", False]));			# False
print();

# 元组tuple
print(any(("a", "b", "c", "d")));	# True
print(any(("a", "b", "", "d")));	# True
print(any((0, "", False)));			# False
print();

print(any([]));
print(any(()));


# python divmod() 函数把除数和余数运算结果结合起来，返回一个包含
# 商和余数的元组(a // b, a % b)
print(divmod(7, 2));
print(divmod(8, 2));
# print(divmod(1+2j, 1+0.5j));


# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted
# 方法返回的是一个新的 list，而不是在原来的基础上进行的操作
a = [5, 7, 6, 3, 4, 1, 2];
b = sorted(a);
print(a);
print(b);

l = [("b", 2), ("a", 1), ("c", 3), ("d", 4)];
# print(sorted(l, (lambda x, y : cmp(x[1], y[1]))));
print(sorted(l, key = lambda x : x[1]));

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)];
print(sorted(students, key = lambda s : s[2]));		# 按年龄排序
print(sorted(students, key = lambda s : s[2], reverse = True));	# 降序