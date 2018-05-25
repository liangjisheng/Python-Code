
# python中二进制，八进制，十六进制
# 2进制以0b开头，0b11为十进制中的3
# 8进制以0o开头，0o11为十进制中的9
# 16进制以0x开头，0x11为十进制中的17
# bin(a) 将数字a转换为二进制
# oct(a) 将数字a转换为八进制
# hex(a) 将数字a转换为十六进制

a = 0b111100;
print(a);

print(bin(a));
print(oct(a));
print(hex(a));

# 在python中是没有++，--运算符的，python不使用++的哲学逻辑：编译解析上的简洁
# 与语言本身的简介。在python中，变量是以内容为基准而不是像C/C++中以变量名为基准
# 所以只要你的数字是5，不管起什么名字，这个变量的ID(变量的内存地址)是相同的
# 同时也说明了pytho中一个变量可以以多个名称访问。
# 这样的设计逻辑决定了python中的数字类型的值是不可变的，如果数字a和b都是5
# 当改变了a时，b也会跟着改变
# 因此如果a要自增应该用a = a + 1，或者a += 1；a自增后，通过id()观察
# id值变化了，即a已经是新值的名称了

num1 = 5;
num2 = 5;
print(num1);
print(num2);
print("id(num1): ", id(num1));
print("id(num2): ", id(num2));
print();

num1 += 1;
print(num1);
print(num2);
print("id(num1): ", id(num1));
print("id(num2): ", id(num2));


input();