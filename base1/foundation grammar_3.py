# 将整个模块导入：import somemodule
# 从某个模块中导入某个函数：from somemodule import somefunction
# 从某个模块中导入多个函数：from somemodule import firstfunc, secondfunc, thridfunc
# 将某个模块中的全部函数导入： from somemodule import *

"""
import sys;
print("==============Python import mode==================");
print("命令行参数为：");
for i in sys.argv:
	print(i);
print("\n python 路径为: ", sys.path);
"""

# 导入sys模块中的argv, path成员
from sys import argv, path;
print("==============Python import mode==================");
# 此处不能加sys，因为并没有导入sys模块
print("path: ", path);