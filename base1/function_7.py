
# bytearray()方法返回一个新字节数组。这个数组里的元素是可变的，
# 并且每个元素的值范围: 0 <= x < 256

print(bytearray());
print(bytearray([1, 2, 3]));
print(bytearray("runoob", "utf-8"));

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数
# 传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放
# 到新列表中
# filter(function, iterable)

def is_odd(n):
	return n % 2 == 1;
	
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
print(newlist);

print(filter(is_odd, range(1, 11)));

# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
# issubclass(class, classinfo)

import math;

print("math.pow(100, 2): ", math.pow(100, 2));
print("pow(100, 2): ", pow(100, 2));
print("math.pow(100, -2): ", math.pow(100, -2));
print("math.pow(2, 4): ", pow(2, 4));
print("math.pow(3, 0): ", pow(3, 0));