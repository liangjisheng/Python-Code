
try:
	sum1 = 1 + '1';		# 数据类型错误
	file = open('no exist.txt');
	file.close();
except OSError as reason:
	print('想要访问的文件不存在\n错误的原因是: ', str(reason));
except TypeError as reason:
	print('数据类型错误\n错误的原因是: ', str(reason));
	
try:
	sum1 = 1 + '1';		# 数据类型错误
	file = open('no exist.txt');
	file.close();
except :
	print('崩溃后没有任何处理');