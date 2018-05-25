
# 内置函数

# ascii()函数类似repr()函数, 返回一个表示对象的字符串, 但是对于字符串中
# 的非ASCII字符则返回通过repr()函数使用 \x, \u 或 \U 编码的字符
# 生成字符串类似Python2版本中repr()函数的返回值

print(ascii("runoob"));

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合
# 为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
# enumerate(sequence, [start=0])

seasons = ["Spring", "Summer", "Fall", "Winter"];
print(seasons);

list1 = list(enumerate(seasons));
print(list1);

# 下标从1开始
list1 = list(enumerate(seasons, 1));
print(list1);

# 普通for循环
i = 0;
seq = ["one", "two", "three"];
for element in seq:
	print(i, seq[i]);
	i += 1;
	
# for循环使用enumerate
for i, element in enumerate(seq):
	print(i, seq[i]);
	
print();

# 转换成8进制字符串
print(oct(10));
print(oct(20));
print(oct(15));

# raw_input() 将所有输入作为字符串看待，返回字符串类型。而input()在
# 对待纯数字输入时具有自己的特性，它返回所输入的数字的类型(int,float)
a = input("input: ");
print(a);
print(type(a));
a = input("input: ");
print(a);
print(type(a));