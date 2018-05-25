
# os模块提供了非常丰富的方法用来处理文件和目录
# os.access(path, mode);
# path -- 要用来检测是否有访问权限的路径
# mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
# os.F_OK: 作为access()的mode参数，测试path是否存在
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行

import os, sys;

ret = os.access("test.txt", os.F_OK);
print("F_OK - 返回值 %s" %ret);

ret = os.access("test.txt", os.R_OK);
print("R_OK - 返回值 %s" %ret);

ret = os.access("test.txt", os.W_OK);
print("W_OK - 返回值 %s" %ret);

ret = os.access("test.txt", os.X_OK);
print("X_OK - 返回值 %s" %ret);

# os.chdir()修改当前工作目录
path = "/test";

# 获取当前工作目录
retval = os.getcwd();
print("当前工作目录 %s " % retval);

path = retval + path;
print(path);
os.chdir(path);

newpath = os.getcwd();
print("当前工作目录 %s " % newpath);

os.chdir(retval);