
# 字典
dict = {"Name":"Runoob", "Age":7, "Class":"First"};
print(dict);
print("dict[\"Name\"]: ", dict["Name"]);
print("dict[\"Age\"]: ", dict["Age"]);
# 如果用字典里没有的键访问数据，则会输出错误

dict["Age"] = 8;
dict["School"] = "liangjisheng";
print(dict);

del dict["Name"];		# 删除键"Name"
print(dict);
dict.clear();			# 删除字典
print(dict);
del dict;
print();

# 字典值可以是任何的 python 对象，既可以是标准的对象，
# 也可以是用户定义的，但键不行
# 不允许同一个键出现两次，创建时如果同一个键被赋值两次，后一个值会被记住
dict = {"Name":"Runoob", "Age":7, "Name":"First"};
print("dict[\"Name\"]: ", dict["Name"]);

print(len(dict));
print(str(dict));

# 字典的键值是只读的，所以不能对键和值分别进行初始化
# 字典是支持无限极嵌套的
citys = {
	"北京" : {
		"朝阳":["国贸", "CBD", "天阶", "我爱我家", "链家地产"],
		"海淀":["圆明园", "苏州街", "中关村", "北京大学"],
		"昌平":["沙河", "南口", "小汤山"],
		"怀柔":["桃花", "梅花", "大山"],
		"密云":["密云A", "密云B", "密云C"]
	},
	"河北":{
		"石家庄":["石家庄A","石家庄B","石家庄C","石家庄D","石家庄E"],
        "张家口":["张家口A","张家口B","张家口C"],
        "承德":["承德A","承德B","承德C","承德D"]
	}
};

print(citys);
print();

for i in citys["北京"]:
	print(i);
print();

for i in citys["北京"]["海淀"]:
	print(i);
print();

input();