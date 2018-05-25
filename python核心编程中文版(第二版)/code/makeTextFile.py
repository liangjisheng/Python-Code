
#!/usr/bin/env python
"makeTextFile.py -- create text file"

import os;
# 类似os.linesep这样的名字解释去需要做两次查询:(1)查找os以确认它是一个模块
# (2):在这个模块中查找lineseq变量
# 可以为os模块的lineseq属性取一个本地变量别名。变量查找速度回快很多，
# 在查找全局变量之前，总是先查找本地变量
ls = os.linesep;	# 行分割符，是一个空行
# print(os.path);
# print(ls);		# 在windows下会输出两个空行

# get filename
while True:
	fname = input("Input filename: ");
	if os.path.exists(fname):
		print("ERROR: %s already exists" % fname);
	else:
		break;

# get file content (text) lines
all = [];
print("Enter lines ('.' by itself to quit).");

# loop until user terminates input
while True:
	# python3中没有raw_input(),统一使用input()返回字符串
	entry = input(">");
	if entry == ".":
		break;
	else:
		all.append(entry);

# write line to file with proper line-ending
fobj = open(fname, "w");
# fobj.writelines(["%s%s" % (x, ls) for x in all]);
fobj.writelines(["%s\n" % x for x in all]);
fobj.close();
print("DONE!");