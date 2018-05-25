
# 字典（dictionary）是Python中另一个非常有用的内置数据类型
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：
# 字典当中的元素是通过键来存取的，而不是通过偏移存取
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key):值(value)对集合
# 键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的

dict = {};
dict["one"] = "1 - testString";
dict[2] = "2 - testint";
tinydict = {"name":"runoob", "code":1, "site":"http://blog.csdn.net/liangjisheng"};

print(dict);
print(dict["one"]);			# 输出键为"one"的值
print(dict[2]);				# 输出键为2的值
print(tinydict);
print(tinydict.keys());		# 输出所有的键
print(tinydict.values());	# 输出所有的值
print();

# 必须将dict对象的引用删除，然后才能使用Python的内置函数
del dict;

dict1 = dict([("runoob", 1), ("google", 2), ("taobao", 3)]);
print(dict1);

input();