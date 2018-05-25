
# 列表推导式
vec = [2, 4, 6];
vec1 = [3 * x for x in vec];

print(vec);
print(vec1);

vec2 = [[x, x**2] for x in vec];
print(vec2);

# 对序列里每一个元素逐个调用某方法
freshfruit = ["   banana  ", "  loganberry  ", "passion fruit  "];
vec3 = [weapen.strip() for weapen in freshfruit];
print(vec3);

# 可以使用if子句作为过滤器
vec4 = [3 * x for x in vec if x > 3];
print(vec4);

vec5 = [3 * x for x in vec if x < 2];
print(vec5);

list1 = [2, 4, 6];
list2 = [4, 3, -9];

list3 = [x * y for x in list1 for y in list2];
print(list3);

list4 = [x + y for x in list1 for y in list2];
print(list4);

list5 = [list1[i] * list2[i] for i in range(len(list1))];
print(list5);

# 列表推导式可以使用复杂表达式或嵌套函数
list6 = [str(round(355 / 113, i)) for i in range(1, 6)];
print(list6);

input();