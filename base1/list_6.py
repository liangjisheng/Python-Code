
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements'];

print(li);
print(li.index("example"));
print(li.index("new"));

# 如果没有的话，会引发一个异常
# li.index("c");

if "c" in li:
	print(li.index("c"));
else:
	print("c no in li");
	
if "z" in li:
	# 如果没有的话，会引发一个异常
	li.remove("z");
else:
	print("z not in li");
	
li = ["a", "b", "mpilgrim"];
print(li);
li = li + ["example", "new"];
print(li);

li = [1, 2] * 3;
print(li);
print();

params = {"Server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"};
print(params.keys());
print(params.values());
print(params.items());
print([k for k, v in params.items()]);
print([v for k, v in params.items()]);

li1 = ["%s = %s" %(k, v) for k, v in params.items()];
print(li1);
s= ";".join(["%s = %s" %(k, v) for k, v in params.items()]);
print(s);

# split与join正好相反，它将一个字符串分割成多元素list
print(s.split(";"));

# 可接受第二个参数，表示要分割的次数
print(s.split(";", 1));

li = [1, 9, 8, 4];
print([elem * 2 for elem in li]);
li = [elem * 2 for elem in li];
print(li);