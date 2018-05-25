input("\n\n按下enter键后退出");

# python 可以在同一行中显示多条语句
import sys; x = "runoob"; sys.stdout.write(x + '\n');

# print()默认输出是换行的，如果要实现不换行需要在变量末尾加上end = " ";
szx = "a";
szy = "b";
# 换行输出
print(szx);
print(szy);

print("-------------");
# 不换行输出
print(szx, end = " ");
print(szy, end = " ");

# 输出一个空行
print();