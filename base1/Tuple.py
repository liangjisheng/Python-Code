
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同

tuple = ("abcd", 786, 2.23, "runoob", 70.2);
tinytuple = (123, "runoob");

print(tuple);
print(tuple[0]);
print(tuple[1:3]);
print(tuple[2:]);
print(tinytuple * 2);
print(tuple + tinytuple);
print();

# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取
tup = (1, 2, 3, 4, 5, 6);
print(tup);
print(tup[0]);
print(tup[1:5]);
# 修改元组元素的操作是非法的，
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ();	# 空元组
tup2 = (20, ); # 一个元素，需要在元素后面添加逗号
print(tup1);
print(tup2);

# string、list和tuple都属于sequence（序列）

input();