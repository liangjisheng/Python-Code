
# 格式化符号进行进制转换
num = 10;

# 加入#号的目的是在转换结果头部显示当前进制类型，如果不需要，可以去掉
print("十六进制: %#x" %num);
print("二进制: ", bin(num));
print("八进制: %#o" %num);

print("十六进制: %x" %num);
print("二进制: ", bin(num));
print("八进制: %o" %num);
print();

# [::2]表示从头走到尾，步长为2
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'd'];
print(list1[::2]);

# 字符串的分割还有partition()这种方式 partition(sep)  --> (head,sep,tail)
# 从左向右遇到分隔符把字符串分割成两部分，返回头、分割符、尾三部分的三元组。
# 如果没有找到分割符，就返回头、尾两个空元素的三元组
s1 = "I'm a good student";
# 以"good"为分割符，返回头、分隔符、尾三部分
s2 = s1.partition("good");
# 没有找到分割符"abc"，返回头、尾两个空元素的元组
s3 = s1.partition("abc");

print(s1);
print(s2);
print(s3);

input();