# Number
# python中有6个标准的数据类型Number, String, List(列表), Tuple(元组), set(集合), Dictionary(字典)
# python3支持int,float, bool, complex(复数)
# 注意:在Python2中是没有布尔型的,它用数字0表示False,用1表示True.到Python3中,
# 把True和False定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加

a, b, c, d = 20, 2.2, True, 4 + 3j;
print(type(a), end = " ");
print(a);

print(type(b), end = " ");
print(b);

print(type(c), end = " ");
print(c);

print(type(d), end = " ");
print(d);
print();

# 除了可以用type显示变量类型外，还可以使用isinstance
print(isinstance(a, int));
print(isinstance(b, float));
print(isinstance(c, bool));
print(isinstance(d, complex));
print();

# isinstance和type的区别在于:
# type()不会认为子类是一种父类类型，isinstance()会认为子类是一种父类类型
class A:
	pass

# 类B继承于A
class B(A):
	pass

print(isinstance(A(), A));	# True
print(type(A()) == A);		# True
print(isinstance(B(), A));	# True
print(type(B()) == A);		# False
print();

# 可以使用del语句删除对象的引用
# del a;	# 打开注释也不报错，可以直接改变变量的类型，说明变量(对象引用)
# 是没有类型，所谓类型是变量所指的内存中对象的类型
del b;
del c, d;

a = "test";
print(a);

# /除法总是返回一个浮点数，要获取整数使用//操作符
c = 2 / 4;
print(c);
print(type(c));

# 除法得到一个整数
c = 2 // 4;
print(c);
print(type(c));

# 取余
c = 17 % 3;
print(c);
print(type(c));

# 乘方
c = 2 ** 5;
print(c);
print(type(c));

input();