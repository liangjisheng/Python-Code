
class FooClass(object):
	"""my very first class: FooClass"""
	version = 0.1		# class (data) attribute
	
	def __init__(self, nm = "John Doe"):
		"""constructor"""
		self.name = nm;		# class instance (data) attribute
		print("Created a class instance for", nm);
		
	def showname(self):
		"""display instance attribute and class name"""
		print("Your name is", self.name);
		print("My name is", self.__class__.__name__);
	
	def showver(self):
		"""display class (static) attribute"""
		print(self.version);	# references FooClass.version
	
	def addMe2Me(self, x):
		"""apply + operation to argument"""
		return x + x;
		
fool = FooClass();
fool.showver();
print(fool.addMe2Me(5));
print(fool.addMe2Me("test "));
fool.showname();
print();

import sys;
sys.stdout.write("hello, world\n");
print(sys.platform);
print(sys.version);
print();

print(dir());		# 显示对象的属性，如果没有提供参数，则显示全局变量的名字
print(dir(fool));
print();

# print(help());
print(help(fool));