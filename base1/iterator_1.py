
# 迭代器是一个可以记住遍历的位置的对象,从集合的第一个元素开始访问，直到所有
# 的元素被访问完结束，迭代器只能往前不会后退，基本的两个方法iter(),next()
# 字符串、列表、元组对象都可用于创建迭代器

list1 = [1, 2, 3, 4];
it = iter(list1);		# 创建迭代器对象
print(next(it));		# 1
print(next(it));		# 2

# 迭代器可以使用常规for语句进行遍历
l2 = list1.copy();
it2 = iter(l2);
for x in it2 :
	print(x, end = " ");
print();
print();
	
l3 = list1.copy();
it3 = iter(l3);
import sys		# 引入sys模块
while True: 
	try : 
		print(next(it3));
	except StopIteration: 
		sys.exit();

input();