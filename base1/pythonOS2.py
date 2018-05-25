
"""获取指定目录及其子目录下的 py 文件路径说明：l 用于存储找到的py文件路径 
get_py 函数，递归查找并存储 py 文件路径于l"""

import os;
import os.path;

l = [];

def get_py(path, l):
	filelist = os.listdir(path);	# 获取path目录下的所有文件
	for filename in filelist:
		# 获取path与filename组合后的路径
		pathTmp = os.path.join(path, filename);
		if os.path.isdir(pathTmp) : # 如果是目录
			get_py(pathTmp, l);		# 则递归查找
		elif filename[-3:].upper() == ".PY": # 不是目录，比较后缀名
			l.append(pathTmp);
	

path = input("请输入路径:").strip();
get_py(path, l);
print("在%s目录及其子目录下找到%d个py文件\n分别是: \n" %(path, len(l)));
for filePath in l:
	print(filePath);