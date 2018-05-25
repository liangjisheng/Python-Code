
# __private_methods

class Site:
	def __init__(self, name, url):
		self.name = name;	# public
		self.__url = url;	# private
	
	def who(self):
		print("name: ", self.name);
		print("url: ", self.__url);
		
	def __foo(self):
		print("这是私有方法");
	
	def foo(self):
		print("这是公共方法");
		self.__foo();
		
x = Site("test", "www.baidu.com");
x.who();
x.foo();
# x.__foo();		# 不能直接访问私有方法