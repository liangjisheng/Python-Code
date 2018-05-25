
# 如果一个异常在try子句里(或者在except和else子句里)被抛出，
# 而又没有任何的except把它截住，那么这个异常会在finally子句执行后再次被抛出

def divide(x, y):
	try :
		res = x / y;
	except ZeroDivisionError:
		print("division by zero");
	else:
		print("res is", res);
	finally:
		print("executing finally clause");

divide(2, 1);
divide(2, 0);
#divide("2", "1");
print();

# 带参数的异常
def temp_convert(var):
	try :
		return int(var);
	except (ValueError) as Argument:
		print("参数没有包含数字\n", Argument);

temp_convert(2.2);
temp_convert("test");