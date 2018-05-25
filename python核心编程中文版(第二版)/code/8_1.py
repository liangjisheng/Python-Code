
def showMaxFactor(num):
	count = num // 2;
	while count > 1:
		if num % count == 0:
			print('largest factor of %d is %d' % (num, count));
			break;
		count -= 1;
	# 如果所有的循环都没有走if的话，也就是break语句没有执行，则会执行else
	# 语句，用于循环后处理；也可以不写这个else语句
	else:
		print(num, 'is prime');
		
#for eachNum in range(10, 21):
	#showMaxFactor(eachNum);
	
# 从根本上说，迭代器就是有一个next()方法的对象，而不是通过索引来计数
# 元素全部取出后，会引发一个StopIteration异常，这并不表示错误发生，
# 只是告诉外部调用者，迭代完成

# map()对所有列表成员应用一个操作
print(list(map(lambda x : x ** 2, range(6))));
print([x ** 2 for x in range(6)]);

seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12];
# filter()基于一个条件表达式过滤列表成员，留下使得lambda表达式为真的列表成员
print(list(filter(lambda x : x % 2, seq)));
# 使用列表解析来完成同样的操作
print([x for x in seq if x % 2]);

# 迭代一个有三行五列的矩阵
print([(x + 1, y + 1) for x in range(3) for y in range(5)]);
print();

f = open('hhga.txt', 'r');
# 输出这个文件有多少行
print(len([line for line in f]));
f.seek(0);
print([line for line in f]);
f.seek(0);
# 输出这个文件中有多少个单词
print(len([word for line in f for word in line.split()]));
f.seek(0);
print([word for line in f for word in line.split()]);

f.seek(0);
# 把每个单词的长度加起来得到和
print(sum([len(word) for line in f for word in line.split()]));
f.close();

import os;
# 快速计算文件大小
print(os.stat('hhga.txt').st_size);