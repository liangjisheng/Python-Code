
# 通常函数运行要输入一组参数，但是也可以把函数编写为一个任务，从而能处理发送
# 给它的一系列输入。这类函数称为协程，可使用yield语句并以表达式(yield)的形式
# 创建协程

def print_matches(matchtext):
	print("Looking for", matchtext);
	while True:
		line = (yield);			# 获得一行文本
		if matchtext in line:
			print(line);
			
matcher = print_matches("python");
matcher.__next__();

# 使用send()为协程发送某个值之前，协程会暂时中止
matcher.send("Hello World");
matcher.send("python is cool");
matcher.send("yow");

# 协程将会继续下去，直到函数返回或者调用它的close()方法为止
matcher.close();