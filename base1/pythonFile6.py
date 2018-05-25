
# writelines() 方法用于向文件中写入一序列的字符串。
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
# 换行需要制定换行符 \n

fo = open("test.txt", "w");
print("文件名: ", fo.name);

seq = ["test1\n", "test2\n"];

fo.writelines(seq);

fo.close();
