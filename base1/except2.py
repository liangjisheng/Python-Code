
# 可以通过创建一个新的exception类来拥有自己的异常。
# 异常应该继承自 Exception 类，或者直接继承，或者间接继承

class MyError(Exception):
	def __init__(self, value):
		self.value = value;
	def __str__(self):
		return repr(self.value);
	
try :
	raise MyError(2 * 2);
except MyError as e:
	print("My exception occurred, value: ", e.value);

	
# try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为
# 不管 try 子句里面有没有发生异常，finally 子句都会执行
try :
	raise KeyboardInterrupt;
finally:
	print("Goodbye, world");