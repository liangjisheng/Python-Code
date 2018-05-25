
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为Python解释器
# 能够用参数名匹配参数值

def printme(str):
	"打印任何传入的字符串"
	print(str);
	return ;
	
printme("test");
printme(str = "test");

# 函数的使用不需要使用指定顺序
def printinfo(name, age):
	"打印任何传入的字符串"
	print("名字: ", name);
	print("年龄: ", age);
	return ;

printinfo("asdf", 10);
printinfo(name = "runoob", age = 50);
printinfo(age = 50, name = "runoob");
print();

# 调用函数时，如果没有传递参数，会使用默认参数,默认参数和C++里面一样
# 必须放在最后
def printinfo1(name, age = 35) :
	"打印任何传入的字符串"
	print("name:", name);
	print("age:", age);
	return ;

printinfo1("runoob");
printinfo1(age = 50, name = "runoob");
print();

# 可能需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数
# 加了*号的变量名会存放所有未命名的变量，如果函数调用时没有指定参数，它
# 就是一个空元组，也可以不向函数传递未命名的变量
def printinfo2(arg1, *vartuple):
	"打印任何传入的字符串"
	print("输出：");
	print(arg1);
	for var in vartuple:
		print(var);
	return ;

printinfo2(10);
printinfo2(70, 60, 50);

input();