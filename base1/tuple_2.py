
# 元组有若干逗号分隔的值组成

t = 12345, 54321, "hello";
print(t);	# 如你所见，元组在输出时总是有括号的，以便于正确表达嵌套结构
# 在输入时可能有或没有括号， 不过括号通常是必须的
# (如果元组是更大的表达式的一部分)
print(t[0]);

u = t, (1, 2, 3, 4, 5);
print(u);
print();


# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素
# 可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用set()
# 而不是 {} ；后者创建一个空的字典
basket = {"apple", "orange", "apple", "pear", "orange", "banana"};
print(basket);

print("orange" in basket);
print("asdf" in basket);

# 下面演示了两个集合的操作
a = set("abracadabra");
b = set("alacazam");
print(a);
print(b);

print(a - b);	# a中唯一的字母
print(a | b);	# 并集
print(a & b);	# 交集
print(a ^ b);	# 在a或b中的字母，但不同时在a和b中

# 集合有支持推导式
a = {x for x in "abracadabra" if x not in "abc"};
print(a);

input();