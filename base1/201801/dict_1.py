
dict1 = dict();
print(dict1);
dict1["sex"] = "male";
dict1["age"] = 9;
dict1["name"] = "Mark";
print(dict1);

dict2 = dict1.copy();
print(dict2);

del dict2["sex"];
print(dict2);

print(dict1);

# 获得sex对应的键值
print(dict1.get("sex"));

# keys()获取字典所有的键
print(dict1.keys());

# values()获取所有的值
print(dict1.values());

# items()获取所有的键值，返回一个列表
print(dict1.items());

# update()更新字典里的某key的值
data = {"age": 33};
dict1.update(data);
print(dict1);

# 如果更新的key原字典里没有，则update就想字典里添加一项数据
data1 = {"age1": 44};
dict1.update(data1);
print(dict1);

d1 = dict(a = 12, dns = "test", c = 13);
print(d1);

value = ["Tom", "Jack", "Rose", "John", "Micheal"]
key = list(range(1, 6));
d2 = dict(zip(key, value))
print(d2);

# pop()可以通过键值删除数据项
d2.pop(2);
print(d2);

# popitem()随机删除一个数据项
d2.popitem();
print(d2);

for x in dict1:
	print(dict1[x]);
	
for (k,v) in dict1.items():
	print("dict1[", k, "] = ", v);