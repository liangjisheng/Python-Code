
# def(**kwargs)把N个关键字参数转换为字典
def func(country, province, **kwargs):
	print(country, province, kwargs);
	
func("China", "Sichuan", city = "Chengdu", section = "JingJiang");

# lambda匿名函数也可以使用关键字参数进行参数传递
g = lambda x, y : x ** 2 + y ** 2;

print(g(2, 3));
print(g(y = 3, x = 2));

# lambda匿名函数也可以设定默认值
g1 = lambda x = 0, y = 0 : x ** 2 + y ** 2;

print(g1(2, 3));
print(g1(y = 3));

# 函数内部可以直接使用全局变量
b = 1;
def ss(a):
	c = a + b;
	print(c);

print(b);
ss(10);

def changeme(mylist):
	"修改传入的列表"
	mylist = [1, 2, 3, 4];
	print("函数内取值:", mylist);
	return ;
	
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值:", mylist);

input();