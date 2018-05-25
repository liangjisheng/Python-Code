
# 内置函数

# 绝对值
print("abs(-40): ", abs(-40));
print("abs(100.10): ", abs(100.10));
print("abs(3+4j): ", abs(3 + 4j));		# 复数求绝对值，返回复数的长度


# dict()创建字典
dict1 = dict();
print(dict1);
dict2 = dict(a = "a", b = "b", t = "t");
print(dict2);

# 以映射方式来构造字典
dict3 = dict(zip(["one", "two", "three"], [1, 2, 3]));
print(dict3);
# 可迭代对象方式来构造字典
dict4 = dict([("one", 1), ("two", 2), ("three", 3)]);
print(dict4);


# 帮助函数
#print(help("sys"));
#print(help("str"));
#a = [1, 2, 3];
#print(help(a));
#print(help(a.append));


# 获取和设置属性值
# getattr(),setattr();
# setattr(object, name, value)
# object -- 对象。
# name -- 字符串，对象属性
# value -- 属性值
class A(object):
	bar = 1;

a = A();
print(getattr(a, "bar"));
setattr(a, "bar", 5);
print(getattr(a, "bar"));


# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为
# 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False
# 如果iterable的所有元素不为0、''、False或者iterable为空，
# all(iterable)返回True，否则返回False；
# 注意：空元组、空列表返回值为True，这里要特别注意
print(all(["a", "b", "c", "d"]));	# 列表list，元素都不为空或0
print(all(["a", "b", "", "d"]));	# 列表list，存在一个为空的元素
print(all([0, 1, 2, 3]));			# 列表list，存在一个为0的元素
print(all(("a", "b", "c", "d")));	# 元组tuple，元素都不为空或0
print(all(("a", "b", "", "d")));	# 元组tuple，存在一个为空的元素
print(all((0, 1, 2, 3)));			# 元组tuple，存在一个为0的元素