
# truncate() 方法用于从文件的首行首字符开始截断，截断文件为size个字符，
# 无 size 表示从当前位置截断；截断之后后面的所有字符被删除，
# 其中Widnows系统下的换行代表2个字符大小

fo = open("runoob.txt", "r+");
print("文件名: ", fo.name);

line = fo.readline();
print("读取行: %s" %(line));

fo.truncate();
line = fo.readlines();
print("读取行: %s" %(line));

fo.close();

# 截取runoob.txt的10个字节
"""
fo = open("runoob.txt", "r+");
print("文件名: ", fo.name);

fo.truncate(10);

str = fo.read();

print("读取数据: %s" %(str));

fo.close();
"""

fo = open("runoob.txt", "r+");
print ("文件名: ", fo.name);

str = "6:www.runoob.com\n";
fo.seek(0, 2);		# 在文件末尾写入一行
line = fo.write(str);

# 读取文件所有内容
fo.seek(0, 0);
for index in range(6):
	line = next(fo);
	print("文件行号 %d - %s" %(index, line));
	
fo.close();