
# python提供了一个办法，把变量或函数的定义存放在文件中，为一些脚本或者
# 交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所以你定义的函数和变量的文件，其后缀名是.py文件，模块可以
# 被别的程序引入，以使用该模块中的函数。这也是使用python标准库的方法

# 内置在每一个python解析器中，变量sys.ps1和sys.ps2定义了主提示符和副提示符
# 所对应的字符串
import sys;

# print(sys.ps1);
# print(sys.ps2);

print("命令行参数如下: ");
for i in sys.argv:
	print(i);
	
# sys.path包含了一个Python解释器自动查找所需模块的路径的列表
print("\n\npython 路径为: ", sys.path, "\n");

# 这样做并没与把直接定义在support.py中的函数写入到当前符号表里，
# 只是把模块support的名字写到了这里，可以使用模块名来访问函数
import support;

support.print_func("runoob");

# 如果打算经常使用这个函数，可以把它赋给一个本地的名称
myprint = support.print_func;
myprint("myprint");

# from ... import 语句可以从模块中导入一个指定的部分到当前命名空间中
# from module import*可以将一个模块的所有内容都导入到当前的命名空间中
from support import sum10;
print(support.sum10());
print(sum10());

# 内置的dir()函数可以找到模块内定义的所有名称，以一个字符串列表的形式返回
print(dir());
print();

print(__builtins__);
print(__cached__);
print(__doc__);
print(__file__);
print(__loader__);
print(__name__);
print(__package__);
print(__spec__);

a = 5;
print(dir());
del a;
print(dir());

input();