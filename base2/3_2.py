
last_names = ["Douglass", "Jefferson", "Williams", "Frank", "Thomas"];

print("%s" %last_names[0]);
print("%s" %last_names[0][0]);
print("%s" %last_names[1]);
print("%s" %last_names[1][0]);
print("%s" %last_names[2]);
print("%s" %last_names[2][0]);
print("%s" %last_names[3]);
print("%s" %last_names[3][0]);
print("%s" %last_names[4]);
print("%s" %last_names[4][0]);
print();

for i in range(len(last_names)):
	print("%s" %last_names[i]);
	print("%s" %last_names[i][0]);
print();

by_letter = {};
by_letter[last_names[0][0]] = last_names[0];
by_letter[last_names[1][0]] = last_names[1];
by_letter[last_names[2][0]] = last_names[2];
by_letter[last_names[3][0]] = last_names[3];
by_letter[last_names[4][0]] = last_names[4];
print();

# 访问列表的最后一个元素
print(last_names[len(last_names) - 1]);
print(last_names[-1]);
print(last_names[-2]);
print(last_names[-3]);