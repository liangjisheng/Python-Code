
# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有

fo = open("runoob.txt", "r+");
print("文件名: ", fo.name);

# 读取10个字节
line = fo.read(10);
print("读取的字符串: %s" %(line));

fo.close();

# readline()方法用于从文件读取整行，包括"\n"字符。如果指定了一个非负数的参数，
# 则返回指定大小的字节数，包括"\n"字符
fo = open("runoob.txt", "r+");
print("文件名: ", fo.name);

line = fo.readline();
print("读取第一行: %s" %(line));

line = fo.readline(5);
print("读取的字符串: %s" %(line));

fo.close();

# readlines()方法用于读取所有行(直到结束符EOF)并返回列表，该列表可以由
# Python的for... in ...结构进行处理。 如果碰到结束符EOF则返回空字符串
fo = open("runoob.txt", "r+");
print("文件名: ", fo.name);

for line in fo.readlines():		# 依次读取每行
	line = line.strip();		# 去掉每行头尾的空白
	print("读取的数据为: %s" %(line));
	
fo.close();

# fileObject.seek(offset[, whence])
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
# whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起