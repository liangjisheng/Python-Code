
# 一般来说，函数的返回值一般是一个
# 而函数返回多个值的时候，是以元组的方式返回的、

def example(a, b):
	return (a, b);

print(type(example(3, 4)));

# python中的函数还可以接受可变参数，比如以*开头的参数名，会将参数收集到一个元组上
def test(*args):
	print(args);
	return args;

print(type(test(1, 2, 3, 4)));

dict1 = dict([("runoob", 1), ("google", 2), ("taobao", 3)]);
dict2 = dict(runoob = 1, google = 2, taobao = 3);
print(dict1);
print(dict2);

# python中的字典是使用了一个称为散列表(hashtable)的算法
# 其特点就是:不管字典中有多少项，insert操作花费的时间都差不多
# 如果把一个字典作为for的迭代对象，那么for循环将会遍历字典的键
def example1(d):
	# d是一个字典对象
	for c in d:
		print(c);

example1(dict1);
print();
example1(dict2);

# 如果想要输出键值对的话，可以这样写
def exam1(d):
	# d是一个字典对象
	for c in d:
		print(c, ":", d[c]);

exam1(dict1);

list1 = ["abcd", 786, 2.23, "runoob", 70.2];
print(list1[1:3]);
print(list1[2]);	# 2.23
print(list1[2:3]);	# [2.23]

# python与C和Java语言的一点不同，表现在它的变量不需要声明变量的类型，这是
# 因为像C和Java语言来说，他们是静态的，而python是动态的，变量的类型有赋予
# 它的值来决定的
a = 1;			# int
a = 1.001;		# float
a = "python";	# String
# 最后输出只保留最后一个的赋值

# type是用于求一个未知数据类型对象，而isinstance是用于判断一个对象是否是
# 已知类型，type 不认为子类是父类的一种类型，而isinstance会认为子类是父类
# 的一种类型。type 与 isinstance 虽然都与数据类型相关，但两者其实用法不同，
# type 主要用于判断未知数据类型，isinstance 主要用于判断A类是否继承于B类
class father(object):
	pass;

class son(father):
	pass;
	
if __name__ == "__main__":
	print(type(son()) == father);
	print(isinstance(son(), father));
	print(type(son()));
	print(type(son));

input();