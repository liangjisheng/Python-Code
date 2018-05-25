
# testFun返回一个列表，列表中存放着4个lambda表达式
def testFun():
	temp = [lambda x : i * x for i in range(4)];
	return temp;
	
for everyLambda in testFun():
	#print(everyLambda);
	#调用列表中的lambda表达式是，传入的值为2，即x=2;因为testFun里面的for
	#循环已经结束，所以i=3;所有下面语句的输出结果为6
	print(everyLambda(2));
print();


#第一种解决方法:创建一个闭包，使用默认参数立即绑定它的参数
def testFun1():
	temp = [lambda x, i = i : i * x for i in range(4)];
	return temp;

for everyLambda in testFun1():
	print(everyLambda(2));
print();

#第二种解决方法
#使用functools.partial函数，把函数的某些参数(不管有没有默认值)给固定住
#(也就是相当于设置默认值)
from functools import partial;
from operator import mul;

def testFun2():
	return [partial(mul, i) for i in range(4)];
	
for everyLambda in testFun2():
	print(everyLambda(2));
print();


# 第三种解决方法:直接用生成器
def testFun3():
	return (lambda x, i = i : i * x for i in range(4));

for everyLambda in testFun3():
	print(everyLambda(2));
print();


# 第四种解决方法:利用yield惰性求值的思想
def testFun4():
	for i in range(4):
		yield lambda x : i * x;
		
for everyLambda in testFun4():
	print(everyLambda(2));
print();