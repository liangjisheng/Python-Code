
# 逻辑运算符

a = 10;
b = 20;

if (a and b) :
	print("a is True, b is True");
else :
	print("a,b 有一个不为True");

if (a or b) :
	print("a和b都为True, 或者其中一个变量为True");
else :
	print("a和b都不为True");
	
a = 0;
if (a and b) :
	print("a,b都为True");
else :
	print("a,b有一个不为True");

if (a or b) :
	print("a和b都为True, 或者其中一个变量为True");
else :
	print("a和b都不为True");

if not(a and b) :
	print("a,b都为false, 或其中一个变量为false");
else :
	print("a,b都为True");

input();