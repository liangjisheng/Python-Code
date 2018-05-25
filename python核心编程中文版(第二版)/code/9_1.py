
# 文件只是连续的字节序列
# 有助于跨平台开发的os模块属性
# linesep 用于在文件中分隔行的字符串
# sep 用来分隔文件路径名的字符串
# pathsep 用于分隔文件路径的字符串
# curdir 当前工作目录的字符串名称
# pardir 父目录字符串名称

import os;

filename = input('Enter file name: ');
fobj = open(filename, 'w');
while True:
	aline = input("Enter a line ('.' to quit): ");
	if aline != '.':
		fobj.write('%s%s' % (aline, os.linesep));
	else:
		break;
fobj.close();