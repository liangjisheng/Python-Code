
# 集合中不包括重复的元素
s = set('cheeseshop');
print(s);
t = frozenset('bookshop');
print(t);

print(type(s));
print(type(t));
print(len(s));
print(len(t));
print(len(s) == len(t));
print(s == t);

for i in s:
	print(i, end = ' ');
print();

s.add('z');
print(s);
s.update('pypi');
print(s);
s.remove('z');
print(s);

s -= set('pypi');
print(s);
print();

print(s | t);		# 并集 union()
print(t | s);
print(s & t);		# 交集 intersection()
print(t & s);
print(s - t);		# 元素在s中，且不再t中 difference()
print(t - s);		# 元素在t中，且不再s中 difference()
print(s ^ t);		# 补集，不同时存在于s和t中 symmetric_difference()
print(t ^ s);