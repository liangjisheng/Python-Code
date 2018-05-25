
#!/usr/bin/env python

# globals()和locals()内建函数分别返回调用者全局和局部名称空间的字典
# 在一个函数内部, 局部名称空间代表在函数执行时候定义的所有名字, 
# locals() 函数返回的就是包含这些名字的字典。 globals() 会返回函数可
# 访问的全局名字。在全局名称空间下, globals() 和 locals() 返回相同的
# 字典, 因为这时的局部名称空间就是全局空间

def foo():
	print("\ncalling foo()...");
	aString = 'bar';
	asInt = 42;
	print("foo()'s globals: ", globals().keys());
	print("foo()'s locals: ", locals().keys());

print("__main__'s globals:", globals().keys());
print("__main__'s locals: ", locals().keys());

foo();
print();

import sys;

# sys.modules变量包含一个有当前载入(完整且成功导入)到解释器的模块组成
# 的字典，模块名作为键，他们的位置作为值
print(sys.modules.keys());