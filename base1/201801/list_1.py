
li1 = [1, 2, 3, 4, 5];
print(li1);

if 2 in li1:
	print("Yes 2 in li1");

if 'x' not in li1:
	print("Yes 'x' not in li1");
	
li1 = li1 * 3;
i = 0;
for val in li1:
	print("li1[%d]"%i, val);
	i += 1;
	
li2 = list(range(1, 10));
print(li2);
li = [x ** 3 for x in li2];
print(li);

# 列表的count()函数可以统计列表里某元素项相同的一共有几个
li = list(range(1, 3));
li1 = li * 3;
print(li1);
print(li1.count(li1[2]));
print(li1.count('a'));

# append()如果添加的对象是列表，列表作为整体添加到列表的尾部
# extend()可以将一个列表的所有元素以个体的方式添加到列表的尾部
li1 = list(range(1, 6));
print(li1);
li2 = list(range(6, 11));
print(li2);
li1.extend(li2);
print(li1);

# remove()函数可以将列表的第一次出现的指定元素删除
li = list(range(1, 4)) * 3;
print("li:", li);
li.remove(2);
print("li:", li);
print();

# pop()函数可以将列表指定位置的元素从列表删除或者将尾部的元素删除
li = list(range(1, 4)) * 3;
print("li:", li);
li.pop();
print("pop:", li);
# 删除下标为3的元素
li.pop(3);
print("pop3:", li);