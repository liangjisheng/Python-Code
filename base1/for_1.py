
languages = ["C", "C++", "Perl", "Python"];
for x in languages : 
	print(x);
	
sites = ["Baidu", "Google", "Runoob", "Taobao"];
for site in sites :
	if site == "Runoob" : 
		print("liangjisheng");
		break;
	print("循环数据: ", site);
else : 
	print("没有循环数据");
print("完成循环")

for i in range(5) : 
	print(i);
print();

for i in range(5, 9) :
	print(i);
print();

for i in range(0, 10, 3) : 
	print(i);
print();

for i in range(-10, -100, -30) : 
	print(i);
print();

for i in range(len(languages)) : 
	print(i, languages[i]);
print();

list1 = list(range(5));
print(list1);

for letter in "Runoob" : 
	if letter == "b" :
		break;
	print("当前字母: ", letter);

var = 10;
while var > 0 : 
	print("当期变量为: ", var);
	var = var -1;
	if var == 5 :
		break;

print("Good Bye");

input();