
# filename: support.py

# 每个模块都有一个__name__属性，当其值为__main__时
# 表明该模块自身在运行，否则是被引入
if __name__ == "__main__":
	print("程序自身在运行");
else:
	print("来自另一个模块");

def print_func(par):
	print("Hello : ", par);
	return ;
	
def sum10(): 
	sum = 0;
	for i in range(10):
		sum += i;
	return sum;
	
def sum100(): 
	sum = 0;
	for i in range(100):
		sum += i;
	return sum;