
# 文件的读写

f = open("foo.txt", "w");
num = f.write("asdf");
f.write("\n");
print(num);
num = f.write("中文字符");
f.write("\n");
print(num);
num = f.write("asdf中文");
f.write("\n");
print(num);

# 如果要写入的不是字符串的东西，那么将需要先进行转换
value = ("test", 14);
s = str(value);
num = f.write(s);
f.write("\n");
print(num);

f.close;

input();