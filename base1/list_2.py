
# 创建二维列表
# list_2d = [[0 for col in range(cols)] for row in range(rows)]
list_2d = [[0 for i in range(5)] for i in range(5)];
list_2d[0].append(3);
list_2d[0].append(5);
list_2d[2].append(7);

print(list_2d);

l = [i for i in range(0, 15)];
print(l);
print(l[::2]);
print();

a = [1, 2, 3];
b = a;
c = [];
c = a;
d = a[:];

# a, b, c三个是同一个ID值，a, b, c的地址是一样的
# 如果像复制得到一个新列表并改变新列表内元素而不影响原列表，可以使用d的赋值方式
print(a);
print(b);
print(c);
print(d);

b[0] = "b";
print(a);
print(b);
print(c);
print(d);

print(id(a));
print(id(b));
print(id(c));
print(id(d));

c[0] = "d";
print(a);
print(b);
print(c);
print(d);

print(id(a));
print(id(b));
print(id(c));
print(id(d));

d[0] = "d";
print(a);
print(b);
print(c);
print(d);

print(id(a));
print(id(b));
print(id(c));
print(id(d));
print();

# 使用copy模块里的copy函数解决列表复制问题
import copy;
lista = [1, 2, 3, 4];
listb = lista;
listd = copy.copy(lista);

print(lista);
print(listb);
print(listd);

print(id(lista));
print(id(listb));
print(id(listd));

# 使用list自带的copy方法，重新开辟内存空间存储新列表
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8];
copy_list = original_list.copy();
copy_list = copy_list + ["a", "b", "c"];
print("original_list: ", original_list);
print("copy_list modify: ", copy_list);
print(id(original_list));
print(id(copy_list));

input();