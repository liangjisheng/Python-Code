
# 标准库
# re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，
# 正则表达式提供了简洁、优化的解决方案

import re;

# 查找以f开头的所有单词
res = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest");
print(res);

res = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat");
print(res);

print("tea fro too".replace("too", "two"));
print();

# 数学
import math;

print(math.cos(math.pi / 4));
print(math.log(1024, 2));
print();

# 随机数
import random;

print(random.choice(["apple", "pear", "banana"]));

# sampling without replacement
print(random.sample(range(100), 10));

# ramdom float
print(random.random());

# random integer chosen from range(6)
print(random.randrange(6));