
# python中的作用域共有4种分别是：L(Local)局部作用域，E(Enclosing)闭包函数外的函数中
# G(Global)全局作用域，B(Built-in)内建作用域，以L->E->G->B的规则查找，

x = int(2.9);		# 内建作用域
g_count = 0;		# 全局作用域

def outer():
	o_count = 1;	# 闭包函数外的函数中
	def inner():
		i_count = 2;	# 局部作用域
		
# python中只有模块(module),类(class),以及函数(def, lambda)才会引入新的作用域
# 其他的代码块(如if/elif/else, try/except, fro/while)是不会引用新的作用域的
# 也就是说，这些语句内定义的变量，外部也可以访问
if True:
	msg = "Runoob";

print(msg);

total = 0;		# 全局变量
def sum(arg1, arg2):
	total = arg1 + arg2;
	print("函数内是局部变量:", total);
	return total;
	
sum(10,20);
print("函数外是全局变量:", total);

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字
num = 1;
def func1():
	global num;	# 需要使用global关键字声明
	print(num);
	num = 123;
	print(num);

func1();

# 如果要修改嵌套作用域(enclosing作用域,外层非全局作用域)中的变量则需要nonlocal关键字了
def outer1():
	num = 10;
	def inner():
		nonlocal num;	# nonlocal关键字声明
		num = 100;
		print(num);
	inner();
	print(num);

outer1();

input();