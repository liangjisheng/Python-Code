
# vars()返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前
# 调用位置的属性和属性值 类似 locals()

print(vars());

class Runoob:
	a = 1;
	
print(vars(Runoob));