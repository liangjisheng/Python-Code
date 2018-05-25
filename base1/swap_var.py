
# 交换两个变量

a = 1;
b = 2;
print("交换变量前a = {0}, b = {1}".format(a, b));

tmp = a;
a = b;
b = tmp;

print("交换变量后a = {0}, b = {1}".format(a, b));

print("再次交换变量");

# 不使用临时变量
a, b = b, a;
print("再次交换变量后a = {0}, b = {1}".format(a, b));