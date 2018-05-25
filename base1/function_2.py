
# 内置函数


print(dir());	# 获得当前模块的属性列表
print();

print(dir([]));	# 查看列表的方法
print();

# 十进制转16进制
print(hex(255));
print(hex(-42));
print(hex(1));

# next() 返回迭代器的下一个项目
# next(iterator[, default])
# iterator -- 可迭代对象
# default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，
# 又没有下一个元素则会触发 StopIteration 异常

it = iter([1, 2, 3, 4, 5]);
while True:
	try:
		# 获取下一个值
		x = next(it);
		print(x);
	except StopIteration:
		# 遇到StopIteration就退出循环
		break;
		
# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递
# class slice(stop)
# class slice(start, stop[, step]) # start -- 起始位置 stop -- 结束位置
# step -- 间距
myslice = slice(5); # 设置截取5个元素的切片
print(myslice);
arr = range(10);
print(arr);
print(arr[myslice]);	# 截取5个元素