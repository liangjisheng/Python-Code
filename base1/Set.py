
# 集合（set）是一个无序不重复元素的序列,基本功能是进行成员关系测试和删除重复元素
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用set()而不是
# { }，因为 { } 是用来创建一个空字典]
# 创建格式parame = {value01,value02,...}或者set(value);

student = {"Tom", "Jim", "Mary", "Tom", "Jack", "Rose"};
print(student);		# 输出集合，重复元素被自动去掉

# 成员测试
if ("Rose" in student):
	print("Rose in student");
else: 
	print("Rose not in student");

# set可以进行集合运算
a = set("abracadabra");
b = set("alacazam");
print(a);
print(b);
print(a - b);	# a和b的差集
print(a | b);	# 并集
print(a & b);	# 交集
print(a ^ b);	# a和b中不同时存在的元素

input();