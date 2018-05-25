
# 判读字符串是否为数字

def is_number(s):
	try :
		float(s);
		return True;
	except ValueError:
		pass;
		
	try:
		import unicodedata;
		unicodedata.numeric(s);
		return True;
	except (TypeError, ValueError):
		pass;
	
	return False;
	
print(is_number("foo"));
print(is_number("1"));
print(is_number("1.3"));
print(is_number("-1.37"));
print(is_number("1e3"));

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False
print();

# str.isdigit() 方法检测字符串是否只由数字组成
# 如果字符串只包含数字则返回 True 否则返回 False

str = "123456";
print(str.isdigit());

str = "runoob example...wow!!!";
print(str.isdigit());