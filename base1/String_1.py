
var1 = "hello world";
var2 = "Runoob";

print(id(var1));
print("var1[0]: ", var1[0]);
print(id(var2));
print("var2[1:5]: ", var2[1:5]);
print(var1[:]);

print("已更新字符串: ", var1[:6] + "Runoob");
print(id(var1));

var1 = "test";
print(id(var1));

a = "hello";
b = "python";

print("a + b 输出结果: ", a + b);
print("a *2 输出结果: ", a * 2);
print("a[1] 输出结果: ", a[1]);
print("a[1:4] 输出结果: ", a[1:4]);

if ("h" in a) :
	print("h in a");
else :
	print("h not in a");
	
if ("m" not in a) :
	print("m not in a");
else :
	print("m in a");	
print();
	
# python中格式化字符串的使用
print("我叫 %s 今年%d岁" %("小明", 10));

# python三引号允许一个字符串跨多行，字符串中可以包含换行符，制表符，及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB(\t).
也可以使用换行符[\n]
"""
print(para_str);

num = 18.7254;
print("the price is %.2f" %num);

num1 = 100000;
print("%g" %(num1));
num1 = 1000000;
print("%g" %(num1));
num1 = 10000000;
print("%g" %(num1));

num1 = 100000.1;
print("%g" %(num1));
num1 = 1.0;
print("%g" %(num1));
num1 = 1.1;
print("%g" %(num1));

input();