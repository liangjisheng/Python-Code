
# random
# 函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b

import random;

print(random.randint(0, 9));

f = open("test.log", "w");

i = 0;
while i < 10000:
	num = random.randint(0, 9);
	str1 = str(num);
	f.write(str1);
	i += 1;

f.close();