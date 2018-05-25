
# 标准库

import os;

print(os.getcwd());		# 当前工作目录

# 执行系统命令ipconfig
os.system("ipconfig");
os.system("mode");

# 建议使用 "import os" 风格而非 "from os import *"。这样可以保证随操作
# 系统不同而有所变化的 os.open() 不会覆盖内置函数 open()

print("os.name: ", os.name);
print("os.path: ", os.path);
print("os.curdir: ", os.curdir);
print("os.pardir: ", os.pardir);
print("os.sep: ", os.sep);
print("os.extsep: ", os.extsep);
print("os.altsep: ", os.altsep);
print("os.pathsep: ", os.pathsep);
print("os.linesep: ", os.linesep);
print("os.defpath: ", os.defpath);
print("os.devnull: ", os.devnull);

# print(dir(os));
# print(help(os));

# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
import glob;

print(glob.glob("*.py"));
print();

# 命令行参数以链表形式存储于 sys 模块的 argv 变量
import sys;

print(sys.argv);

sys.stderr.write("Warning log file not found starting a new one\n");