
# 成员运算符

a = 10;
b = 20;
l1 = [1, 2, 3, 4, 5];

if (a in l1) :
	print("a in l1");
else :
	print("a not in l1");

if (b in l1) :
	print("b in l1");
else :
	print("b not in l1");
	
a = 2;
if (a in l1) :
	print("a in l1");
else :
	print("a not in l1");

input();