
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，
# 类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例

class people:
	# 定义基本属性
	name = "";
	age = 0;
	# 定义私有属性，私有属性在类外部无法直接进行访问
	__weight = 0;
	# 定义构造方法
	def __init__(self, n, a, w):
		self.name = n;
		self.age = a;
		self.__weight = w;
	def speak(self):
		print("%s 说: 我 %d 岁" %(self.name, self.age));

p = people("runoob", 10, 30);
p.speak();