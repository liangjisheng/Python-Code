
a = 2;
import sys;

# 获得对象的当前引用计数
print(sys.getrefcount(a));

a = [1, 2, 3, 4];
b = a;
print(b is a);	# True
print(a);

b[2] = -100;
print(a);
print();

a = [1, 2, [3, 4]];
# 创建a的一个浅复制 a,b是不同的对象，但包含的是原始对象中包含的项的引用
b = list(a);
print(b is a);		# False
print("a = ", a);

b.append(100);
print("b = ", b);
print("a = ", a);

b[2][0] = -100;
print("b = ", b);
print("a = ", a);
print();

import copy;
a = [1, 2, [3, 4]];
b = copy.deepcopy(a);
print("a = ", a);
print("b = ", b);

b[2][0] = -100;
print("a = ", a);
print("b = ", b);
print();

line = "GOOG, 100, 490.10";
filed_types = [str, int, float];
raw_fields = line.split(',');
fields = [ty(val) for ty, val in zip(filed_types, raw_fields)];
print(fields);