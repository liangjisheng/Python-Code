
# python使用lambda来创建匿名函数,所谓匿名，意为不在使用def语句这样标准的形式
# 定义一个函数
# lambda 只是一个表达式，函数体比 def 简单很多
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装
# 有限的逻辑进去
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是
# 调用小函数时不占用栈内存从而增加运行效率

sum = lambda arg1, arg2 : arg1 + arg2;

print("相加后的值为:", sum(10, 20));
print("相加后的值为:", sum(20, 10));

def sum1(arg1, arg2):
	# 返回两个参数的和
	total = arg1 + arg2;
	print("函数内:", total);
	return total;
	
total = sum1(10, 20);
print("函数外:", total);
print();

input();