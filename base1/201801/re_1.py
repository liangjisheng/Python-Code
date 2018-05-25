
# 正则表达式
import re;
# 元字符：一次只能匹配一个字符或者一个位置，元字符分为匹配字符的元字符和
# 匹配位置的元字符
# 1.匹配字符的元字符
# ^string匹配所有以string开头的行
# string$匹配所有以string结尾的行
# ^$可以匹配空行
# \bStr,\b可以实现匹配以Str开始的单词
# Str\b匹配以Str结尾的单词
# 2.匹配位置的元字符
# \w匹配单词里的字符(字母，数字，下划线)
# \W匹配单词里的非字符
# \d匹配数字
# \D匹配非数字字符
# \s匹配空格字符
# \S匹配非空格字符

# 匹配以jea开头
s = "hello www jeapedu com world";
res = r"\bjea";
print(re.findall(res, s));
s = "help jeap jeep jeapedu jeapedu.com";
print(re.findall(res, s));

# 匹配以eap结尾
s = "help jeap jeep jeapedu jeapedu.com";
res = r"eap\b";
print(re.findall(res, s));
print();

# 匹配含hello的行
s = """
ahello
www jeapedu com hellob world

helloc world
nice hellod world
piece of helloe world jeapedu
"""
res = r"\hello";
print("hello ", re.findall(res, s));

# 匹配含字母和数字
s = "a1b2c3d";
res = "\w\d";
print(re.findall(res, s));
res = "\w\d\w";
print(re.findall(res, s));