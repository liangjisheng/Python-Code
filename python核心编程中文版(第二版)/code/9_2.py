
f = open('test.txt', 'w+');
print(f);
print(f.tell());	# 返回文件内指针的位置
f.write('test line 1\n');
print(f.tell());
f.write('test line 2\n');
print(f.tell());

# 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算
# 相对位置，从文件尾计算时就会引发异常
# f.seek(12, 1);		# 从当前位置向后移动12个字节
print(f.tell());
print(f.readline());

f.seek(0, 0);		# 回到文件的最开始
print(f.readline());
print(f.tell());
print(f.readline());
print(f.tell());

f.close();