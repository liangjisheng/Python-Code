
# 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以
# 是任意不可变类型，通常用字符串或数值。
# 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，
# 关键字必须是互不相同。一对大括号创建一个空的字典：{}

tel = {"Jack" : 4098, "sape" : 4139};
tel["guido"] = 4127;
print(tel);

print(tel["Jack"]);

del tel["sape"];
tel["irv"] = 4127;
print(tel);

list1 = list(tel.keys());
print(list1);

list2 = sorted(tel.keys());
print(list2);

print("guido" in tel);
print("Jack" not in tel);
print();

dict1 = dict([("sape", 4139), ("guido", 4127), ("Jack", 4098)]);
print(dict1);

dict2 = {x: x ** 2 for x in (2, 4, 6)};
print(dict2);

dict3 = dict(sape = 1, guido = 2, jack = 3);
print(dict3);
print();

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {"gallahad" : "the pure", "robin" : "the brave"};
for k, v in knights.items() : 
	print(k, v);

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(["tic", "tac", "toe"]):
	print(i, v);

input();