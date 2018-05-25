
# 捕捉依次后，程序并不会终止，而是继续下执行
try:
	f = open("file.txt", "r");
except IOError as e:
	print(e);

print("asdf");

# __doc__属性描述了某个函数的用途说明
print(issubclass.__doc__);
print(print.__doc__);