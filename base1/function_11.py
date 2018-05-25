
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，
# 返回包含每次 function 函数返回值的新列表

def square(x):
	return x ** 2;
	
print(map(square, [1, 2, 3, 4, 5]));

# 使用lambda匿名函数
print(map(lambda x : x ** 2, [1, 2, 3, 4, 5]));

# 提供了两个列表，对相同位置的列表数据进行相加
list1 = map(lambda x, y : x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]);
print(list1);

# reversed 函数返回一个反转的迭代器
# reversed(seq)seq -- 要转换的序列，可以是 tuple, string, list 或 range
# 返回一个反转的迭代器
seqString = "Runoob";
print(list(seqString));
print(list(reversed(seqString)));

# tuple
seqTuple = ("R", "u", "n", "o", "o", "b");
print(list(seqTuple));
print(list(reversed(seqTuple)));

# range
seqRange = range(5, 9);
print(list(seqRange));
print(list(reversed(seqRange)));

# hash()用于获取取一个对象（字符串或者数值等）的哈希值
print(hash("test"));
print(hash(1));
print(hash(str([1, 2, 3])));
print(hash(str(sorted({"1":1}))));

# memoryview() 函数返回给定参数的内存查看对象(Momory view)
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象
# 基础上允许Python代码访问

v = memoryview(bytearray("abcdefg", "utf-8"));
print(v[1]);
print(v[-1]);
print(v[1:4]);
print(v[1:4].tobytes());