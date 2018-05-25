
# is 是判断两个标识符是不是引用自一个对象 x is y, 类似 id(x) == id(y)
# is not 是判断两个标识符是不是引用自不同对象
# id()函数用于获取对象内存地址

a = 20;
b = 20;

if (a is b) :
	print("a,b有相同的标识");
else :
	print("a,b没有相同的标识");

if (id(a) == id(b)) :
	print("a,b有相同的标识");
else :
	print("a,b没有相同的标识");
	
b = 30;
if (a is b) :
	print("a,b有相同的标识");
else :
	print("a,b没有相同的标识");

if (id(a) == id(b)) :
	print("a,b有相同的标识");
else :
	print("a,b没有相同的标识");
	
print();

# is 与 == 的区别
# is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等
l1 = [1, 2, 3];
l2 = l1;
print("l1: ", l1);
print("l2: ", l2);

if (l1 is l2) :
	print("l1 is l2");
else :
	print("l1 is not l2");

l2 = l1[:];
print("l1: ", l1);
print("l2: ", l2);

if (l1 is l2) :
	print("l1 is l2");
else :
	print("l1 is not l2");
	
if (l1 == l2) :
	print("l1 is l2");
else :
	print("l1 is not l2");
	
input();