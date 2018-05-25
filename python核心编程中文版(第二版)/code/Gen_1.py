
#!/usr/bin/env python

def simpleGen():
	yield 1;
	yield '2 --> punch!';
	
myG = simpleGen();
print(next(myG));
print(next(myG));

# 当到达一个真正的返回或者函数结束没有更多的值返回是,StopIteration
# 异常就会抛出
# print(next(myG));

for eachItem in simpleGen():
	print(eachItem);
print();

from random import randint;

def randGen(aList):
	while len(aList) > 0:
		yield aList.pop(randint(0, len(aList) - 1));
		
for item in randGen(['rock', 'paper', 'scissors']):
	print(item);