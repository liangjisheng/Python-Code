
items = [2, 3];
items.append(73);
print(items);

# dir()函数可以列出对象上的可用方法
print(dir(items));

print(items.__add__([4, 5]));
print(items);
print();

class Stack(object):
	# 双下划线开头和结尾的方法是特殊的方法
	def __init__(self):
		self.stack = [];
	def push(self, object):
		self.stack.append(object);
	def pop(self):
		return self.stack.pop();
	def length(self):
		return len(self.stack);
		
s = Stack();
s.push("asdf");
s.push(32);
s.push([3, 4, 5]);
x = s.pop();
print(x);
y = s.pop();
print(y);
del s;