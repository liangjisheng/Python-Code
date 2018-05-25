
# 正则表达式

import re;

print(re.match("www", "www.runoob.com").span());	# 在起始位置匹配
print(re.match("com", "www.runoob.com"));	# 不在起始位置匹配

line = "Cats are smarter than dogs";

matchObj = re.match(r"(.*) are (.*?) .*", line, re.M | re.I);

if matchObj:
	print("matchObj.group(): ", matchObj.group());
	print("matchObj.group(1): ", matchObj.group(1));
	print("matchObj.group(2): ", matchObj.group(2));
else:
	print("No match");
	

# re.search 扫描整个字符串并返回第一个成功的匹配
# re.search(pattern, string, flags=0)
# 匹配成功re.search方法返回一个匹配的对象，否则返回None

print(re.search("www", "www.runoob.com").span());	# 在起始位置匹配
print(re.search("com", "www.runoob.com").span());	# 不在起始位置匹配

searchObj = re.search(r"(.*) are (.*?) .*", line, re.M | re.I);

if searchObj:
	print("searchObj.group(): ", searchObj.group());
	print("searchObj.group(1): ", searchObj.group(1));
	print("searchObj.group(2): ", searchObj.group(2));
else:
	print("Nothing found");
print();

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
# 则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配

matchObj1 = re.match(r"dogs", line, re.M | re.I);
if matchObj1:
	print("match --> matchObj1.group(): ", matchObj1.group());
else:
	print("No match");
	
matchObj1 = re.search(r"dogs", line, re.M | re.I);
if matchObj1:
	print("search --> matchObj1.group(): ", matchObj1.group());
else:
	print("No match");