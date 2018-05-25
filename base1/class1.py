
# 类提供了面向对象编程的所有基本功能: 类的继承机制允许多个基类，派生类可以
# 覆盖基类中的任何方法，方法中可以调用基类中的同名方法

class MyClass:
	"""一个简单的类实例"""
	i = 12345;
	# self代表类的实例，而非类，作用相当于C++中的this指针
	def f(self):
		return "hello, world";
		
# 实例化类
x = MyClass();

# 访问类的属性和方法
print("MyClass 类的属性 i 为: ", x.i);
print("MyClass 类的方法 f 输出为: ", x.f());

# 类具有__init__()方法，类的实例化会自动调用__init__()方法
# __init__()可以有参数，参数通过 __init__() 传递到类的实例化操作上

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart;
		self.i = imagpart;

x = Complex(3.0, -4.5);
print(x.r, x.i);

# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的
# 第一个参数名称, 按照惯例它的名称是 self
# self代表类的实例，代表当前对象的地址，而self.calss则指向类
class Test:
	def prt(self):
		print(self);
		print(self.__class__);

t = Test();
t.prt();

# self不是python关键字，把它换成runoob也是可以的
class Test1:
	def prt(runoob):
		print(runoob);
		print(runoob.__class__);
		
t1 = Test1();
t1.prt();