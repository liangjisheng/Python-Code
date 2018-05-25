
# 一般单引号里可以有双引号，双引号里可以有单引号，
# 三引号里可以有单引号和双引号
s = "Hello 'jack'...";
print(s);

s = "Hello \"jack\"...";
print(s);

s = '''hello "jack"...''';
print(s);

s = """hello "jack"...""";
print(s);

# 原始字符串
s = r"D:\test\node";
print(s);

# s.index(sub[,start[,end]]);	定位子串sub在s里第一次出现的位置，找不到会报错
# s.find(sub[,start[,end]]);	与index一样，但如果找不到会返回-1
# s.replace(old, new[,count]);	替换s里所有old子串为new子串，count指定多少个可以被替换
# s.count(sub[,start[,end]]);	统计s里有多少个sub子串
# s.split([sep[,maxsplit]]);	用sep分割s字符串，默认空格分隔，返回由单词组成的列表

s = "www.jeapedu.com" * 5;
n = s.count("jeapedu");
print(n);
pos = -1;
i = 0;
# 如果将i<n改成i<=n,就会因为多循环查找一次而报错
while i < n:
	pos = s.index("jeapedu", pos + 1);
	print('find "jeapedu" in s:', pos);
	i += 1;
	
s = "www.jeapedu.com" * 3;
print(s);
# 将前两个j替换为J
s = s.replace('j', 'J', 2);
print(s);

print(s[s.find('j')]);