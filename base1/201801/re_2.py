
import re;
# re模块提供了一个正则表达式引擎的接口，可以将正则表达式(字符串)编译
# (re.compile函数)成re模块可以使用、处理的实例对象并用它调用各种函数
# 来进行正则匹配
# 一旦有了已经编译了的正则表达式的实例对象，就可以以实例对象调用mathc
# search,findall,split等函数进行正则匹配了

s = "hello www.baidu.com";
res = "[\s\.]";
pat = re.compile(res);
print(pat.findall(s));
print(pat.split(s));

print(re.findall(res, s));
print(re.split(res, s));