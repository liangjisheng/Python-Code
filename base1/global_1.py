
# 如果函数想读取全局变量，直接使用即可。但如果想在某个函数里面修改某个全局
# 变量的话，需要在修改前用global语句声明一下这个变量是全局的才能修改

def printLocalx():
	x = 12;
	print("f1 local x = ", x);
	
def printLocaly():
	y = 13;
	print("f2 local y = ", y);

def readGlobal():
	print("f3 read global x = ", x);
	print("f3 read global y = ", y);

def modifyGlobal():
	global x;
	print("f4 write x = -1");
	x = -1;

def main():
	printLocalx();
	printLocaly();
	readGlobal();
	modifyGlobal();
	
x = 200;
y = 100;

main();

print("after modified global x = ", x);
print("End");