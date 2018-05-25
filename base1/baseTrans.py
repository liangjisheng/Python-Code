
# 进制转换

num = int(input("输入数字: "));

print("十进制数字: ", num);
print("转换为二进制:", bin(num));
print("转换为八进制: ", oct(num));
print("转换为十六进制: ", hex(num));

# ASCII码与字符相互转换
c = input("请输入一个字符: ");
a = int(input("请输入一个ASCII码: "));

print(c + " 的ASCII码为", ord(c));
print(a, " 对应的字符为: ", chr(a));