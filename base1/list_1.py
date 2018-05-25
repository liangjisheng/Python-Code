
# python中有6个序列的内置类型，最常见的是列表和元组
# 列表的数据项不需要具有相同的类型

list1 = ["google", "runoob", 1997, 2000];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"];

print(list1);
print(list2);
print(list3);

list1[2] = 2001;
print(list1);

# 使用del语句来删除列表的元素
del list1[2];
print(list1);

print(len(list1));
print(list1 + list2);
print(list1 * 2);

if 3 in [1, 2, 3]:
	print("True");
else: 
	print("False");
	
for x in [1, 2, 3]:
	print(x, end = " ");
print();

# 列表支持拼接	
list1 = [1, 2, 3] + list1;
print(list1);

# 使用嵌套列表，在列表中创建其他列表
a = ["a", "b", "c"];
n = [1, 2, 3];
x = [a, n];
print(x);
print(x[0]);
print(x[1]);
print(x[0][1]);

input();