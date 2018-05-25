
# 元组与列表类似，不同之处在于元组的元素不能修改
# 元组使用小括号，列表使用方括号

tup1 = ("google", "runoob", 1997, 2000);
tup2 = (1, 2, 3, 4, 5);
tup3 = "a", "b", "c", "d";

print(tup1);
print(tup2);
print(tup3);

print("tup1[0]: ", tup1[0]);
print("tup2[1:5]: ", tup2[1:5]);

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tuple1 = tup1 + tup2;
print(tuple1);

# tup1 = ();	# 创建空元组
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当做运算符使用
tup4 = (50);
print(type(tup4));
tup5 = (50,);
print(type(tup5));

# 原则中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup1;
print("删除后的元组tup1: ");
# 不能删除被删除的元组
# print(tup1);

print(len(tup2));
tup2 = (6, 7, 8, 9) + tup2;
print(tup2);
print(tup2 * 2);

if 5 in tup2: 
	print("True");
else:
	print("False");
	
if 11 in tup2:
	print("True");
else:
	print("False");
	
for x in tup2 :
	print(x, end = " ");
print();

# 只有一个元素的tuple时，需要即一个逗号，以免误解成数学计算意义上的括号

# 现在来看一个可变的tuple
t = ("a", "b", ["A", "B"]);
print(t);
t[2][0] = "X";
t[2][1] = "Y";
print(t);
# tuple定义的时候有3个元素，分别是"a","b"和一个list，不是说tuple一旦定义了
# 就不能改变了？怎么现在又改变了？
# 定义tuple的时候，包含3个元素，当我们把list的元素"A"和"B"修改之后，tuple
# 变为:从表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list
# 的元素，tuple一开始指向的list并没有改成别的list，所以tuple所谓的"不变"是
# 说，tuple的每个元素，指向永远不变。即指向"a",就不能改成指向"b",指向一个
# list,就不能改成指向其他对象，但指向的这个list本身是可变的！要创建一个内容
# 也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变
input();