
#/usr/bin/env python
#如果在一个内部函数里，对在外部作用域(但不是在全局作用域）的变量进行引用，
#那么内部函数就被认为是 closure。定义在外部函数内的但由内部函数引用或者
#使用的变量被称为自由变量。closures 在函数式编程中是一个重要的概念，
#Scheme 和 Haskell 便是函数式编程中两种

#闭包也是函数，但是他们能携带一些额外的作用域。
#它们仅仅是带了额外特征的函数……另外的作用域

def counter(start_at = 0):
	count = [start_at];
	def incr():
		count[0] += 1;
		return count[0];
	return incr;
	
count = counter(5);
print(count());
print(count());

count2 = counter(100);
print(count2());
print(count());