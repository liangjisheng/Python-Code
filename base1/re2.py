
# 正则表达式
import re;

# Python 的re模块提供了re.sub用于替换字符串中的匹配项
# re.sub(pattern, repl, string, count=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配

phone = "2004-959-559 # 这是一个电话号码";

# 删除注释
num = re.sub(r"#.*$", "", phone);
print("电话号码: ", num);

# 移除非数字的内容
num = re.sub(r"\D", "", phone);
print("电话号码: ", num);


# repl参数是一个函数
# 将匹配的数字乘以2
def myDouble(mathced):
	value = int(mathced.group("value"));
	return str(value * 2);

s = "A23G4HFD567";
print(s);
print(re.sub("(?P<value>\d+)", myDouble, s));

# 改变日期的格式，如中国格式 2017-11-27 改为美国格式 11/27/2017
# 用 () 来划定原字符串的组，{} 中表示数字的个数，r即后面的字符串为
# 原始字符串，防止计算机将\理解为转义字符，2,3,1为输入的字符串三段的序号
s = '2017-11-27'
print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', s))