
# super()解决多重继承问题

class FooParent(object):
	def __init__(self):
		self.parent = "I\'m the parent";
		print("Parent");
		
	def bar(self, message):
		print("%s from Parent" %message);

class FooChild(FooParent):
	def __init__(self):
		super(FooChild, self).__init__();
		print("Child");
	
	def bar(self, message):
		super(FooChild, self).bar(message);
		print("Child bar function");
		print(self.parent);
		
if __name__ == "__main__":
	fooChild = FooChild();
	fooChild.bar("Hello World");
	
print();

# 不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"));
# 设置指定位置
print("{0} {1}".format("hello", "world"));
# 设置指定位置
print("{1} {0} {1}".format("hello", "world"));

print("网站名 {name}, 地址 {url}".format(name = "test", url = "www.baidu.com"));

# 通过字典设置参数
site = {"name":"test", "url":"www.baidu.com"};
print("网站名 {name}, 地址 {url}".format(**site));

# 通过列表索引设置参数
my_list = ["test", "www.baidu.com"];
# "0" 是必须的
print("网站名:{0[0]}, 地址:{0[1]}".format(my_list));
print();

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的