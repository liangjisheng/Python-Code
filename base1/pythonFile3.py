
fo = open("runoob.txt", "wb");
print("文件名为:", fo.name);

# 清空文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 
# 而不是被动的等待输出缓冲区写入
fo.flush();

# fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，
# 可用于底层操作系统的 I/O 操作
fid = fo.fileno();
print("文件描述符: ", fid);

# isatty() 方法检测文件是否连接到一个终端设备，如果是返回True，否则返回False
ret = fo.isatty();
print("isatty: ", ret);

fo.close();

# Python3中的File对象不支持next()方法。Python3的内置函数next()通过迭代器
# 调用__next__()方法返回下一项。在循环中，next()方法会在每次循环中调用，
# 该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration
fo = open("runoob1.txt", "r");

for index in range(5):
	line = next(fo);
	print("第%d行 - %s" %(index, line));

fo.close();