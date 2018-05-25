
# 类的专有方法
# __init__:构造函数，在生成对象时调用
# __del__:析构函数，在释放对象时调用
# __repr__:打印，转换
# __setitem__:按照索引赋值
# __getitem__:按照索引获取值
# __len__:获得长度
# __cmp__:比较运算
# __call__:函数调用
# __add__:加
# __sub__:减
# __mul__:乘
# __div__:除
# __mod__:求余运算
# __pow__:乘方

# Python同样支持运算符重载，我们可以对类的专有方法进行重载

class Vector:
	def __init__(self, a, b):
		self.a = a;
		self.b = b;
	
	def __str__(self):
		return "Vector (%d, %d)" %(self.a, self.b);
		
	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b);
		
v1 = Vector(2, 10);
v2 = Vector(5, -2);
print(v1 + v2);

# 重载__str__
class people:
	def __init__(self, name, age):
		self.name = name;
		self.age = age;
	
	def __str__(self):
		return "name = %s, age = %d" %(self.name, self.age);

a = people("孙悟空", 999);
print(a);

# 没有重载__str__
class people1:
	def __init__(self, name, age):
		self.name = name;
		self.age = age;
		
a1 = people1("test", 999);
# 输出: <__main__.people1 object at 0x000001F126C65198>
print(a1);