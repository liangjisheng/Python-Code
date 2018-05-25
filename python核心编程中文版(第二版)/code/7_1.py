
fdict = dict((['x', 1], ['y', 2]));
print(fdict);

# 内建方法fromkeys()来创建一个默认字典，字典中元素具有相同的值
# 如果没有给出，默认为None
ddict = {}.fromkeys(('x', 'y'), -1);
print(ddict);
ddict = {}.fromkeys(('x', 'y'), (-1, -2));
print(ddict);
edict = {}.fromkeys(('foo', 'bar'));
print(edict);
print();

dict2 = {'name':'earth', 'port':80, 'test':23};
for key in dict2.keys():
	print('key = %s, value = %s' %(key, dict2[key]));
print();

# 可以使用迭代器来访问类序列对象(sequence-like objects),比如字典和文件
for key in dict2:
	print('key = %s, value = %s' %(key, dict2[key]));
	
dict2['name'] = 'venus';
dict2['port'] = 6969;
dict2['arch'] = 'sunos5';
print(dict2);
print(dict2.keys());
print(dict2.values());
print(dict2.items());
print();

for eachKey in sorted(dict2):
	print('dict2 Key', eachKey, 'has value', dict2[eachKey]);
	
print('server' in dict2);
print('name' in dict2);
print(dict2['name']);
print();

dict3 = {};
dict3[1] = 'abc';
dict3[2] = 3.14159;
dict3[3.2] = 'xyz';
print(dict3);

print(dict(zip(('x', 'y'), (1, 2))));
print(dict([['x', 1], ['y', 2]]));
print(dict([('xy'[i - 1], i) for i in range(1, 3)]));
print();

# 值相等的数字的哈希值是相同的
print(hash(1));
print(hash(1.0));