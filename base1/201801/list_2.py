
# 删除列表里重复的元素
li = "jeapedu" * 100;
li = list(li);
li.sort();
print(li);

i = 0;
for s in li:
	print(i, s);
	while li.count(s) > 1:
		li.remove(s);
	i += 1;
	print(li);

print("有%d个不重复的元素" %i);

t = tuple(range(1, 11));
print(t);