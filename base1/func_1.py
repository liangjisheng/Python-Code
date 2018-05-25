
# 函数的第一行语句可以选择性的使用文档字符串--用于存放函数说明
# return结束函数，选择性的返回一个值给调用方，不带表达式的return相当于返回None

def hello() :
	print("hello, world");
	
hello();

def area(width, height) : 
	return width * height;
	
def print_welcome(name): 
	print("Welcome ", name);
	
print_welcome("Runoob");

w = 4;
h = 5;
print("width =", w, "height =", h, "area =", area(w, h));


# 在python中，类型属于对象，变量是没有类型的
# a = [1, 2, 3];
# a = "Runoob";
# 上面代码中，[1, 2, 3]是list类型，"Runoob"是String类型，而变量a是没有类型
# 它仅仅是一个对象的引用(一个指针),可以是list类型对象，也可以指向String类型对象

# 可更改(mutable)与不可更改对象(immutable)
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
# 而 list,dict 等则是可以修改的对象
# 不可变类型：变量赋值a=5后再赋值a=10，这里实际是新生成一个int值对象10，
# 再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值la[2]=5则是将list la的第三个元素值
# 更改，本身la没有动，只是其内部的一部分值被修改了

# 参数传递
# 不可变类型：类似c++的值传递，如 整数、字符串、元组。如fun(a)，传递的只
# 是a的值，没有影响a对象本身。比如在fun(a)内部修改a的值，只是修改另一个
# 复制的对象，不会影响a本身。
# 可变类型：类似c++的引用传递，如列表，字典
# 如fun(la)，则是将la真正的传过去，修改后fun外部的la也会受影响

# python中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说
# 传不可变对象和传可变对象

# 传不可变对象
def changeInt(a):
	print(id(a));
	a = 10;
	print(id(a));
	print(a);
	
b = 2;
print(id(b));
changeInt(b);
print(id(b))
print(b);

# 传可变对象
def changeme(mylist):
	"修改传入的列表"
	mylist.append([1, 2, 3, 4]);
	print("函数内取值:", mylist);
	return ;
	
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值:", mylist);

input();