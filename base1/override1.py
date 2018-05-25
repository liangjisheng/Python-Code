
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法

class parent:
	def myMethod(self):
		print("调用父类方法");

class child(parent):
	def myMethod(self):
		print("调用子类方法");
		
c = child();
c.myMethod();

# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被
# 使用或直接访问。在类内部的方法中使用时 self.__private_attrs
# self的名字并不是规定死的，也可以使用this，但是最好还是按照约定是用self
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部
# 调用 ，不能在类地外部调用。self.__private_methods
class JustCounter:
	__secretCount = 0;		# 私有变量
	publicCount = 0;		# 公开变量
	
	def count(self):
		self.__secretCount += 1;
		self.publicCount += 1;
		print(self.__secretCount);
		
counter = JustCounter();
counter.count();
counter.count();
print(counter.publicCount);
# print(counter.__secretCount);		# 不能直接访问私有变量