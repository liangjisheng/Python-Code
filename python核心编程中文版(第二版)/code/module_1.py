
# 通常只有主程序模块中有大量顶级可执行代码(没有缩进)，所有其他被导入的
# 模块只应该有很少的顶级执行代码，所有的功能代码都应该封装在函数或类当中

# /usr/bin/env python
"this is a test module"		# module documentation

import sys;
import os;

debug = True;

class FooClass(object):
	"Foo class"
	pass;
	
def test():
	"test function"
	foo = FooClass();
	
	if debug:
		print("ran test()");

# 无论这个模块是被别的模块导入还是作为脚本直接运行，都会执行这部分代码
# 通常这里不会有太多的功能性代码，而是根据执行的模式调用不同的函数		
# __name__能在运行时检测模块是被导入还是被直接执行，如果是被导入__name__
# 的值为模块名字，如果模块被直接执行__name__的值为__main__
if __name__ == "__main__":
	test();
elif __name__ != "__main__":
	print("__main__");
	
print(sys.__name__);	# sys
print(os.__name__);		# os