
# 类型对象，NULL对象
print(type(42));
print(type(type(42)));	# 输出类型对象的类型

# 所有标准对象均可用于布尔测试，同类型的对象之间可以比较大小
# 代码对象是编译过的 Python 源代码片段，它是可执行对象。通过调用内建函数 compile()
# 可以得到代码对象。代码对象可以被 exec 命令或 eval()内建函数来执行

a = b = 4;
print(id(a));
print(id(b));
print(a is b);	# 和下一行代码等价
print(id(a) == id(b));
print(a is not b);
print();

c = 1.0;
d = 1.0;
print(id(c));
print(id(d));
print(c is d);