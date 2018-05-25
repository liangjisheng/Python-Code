# -*- coding:utf-8 -*-
"""
@project = 0520-1
@file = str_1
@author = Liangjisheng
@create_time = 2018/5/20 0020 上午 9:14
"""
# __add__函数 (在后面追加字符串)
s1 = 'hello'
s2 = s1.__add__(' boy!')
print(s2)

# __contains__（判断是否包含某字符串，包含则返回True）
result = s1.__contains__('he')
print(result)
s2 = 'how'
result = s1.__eq__(s2)
print(result)

# __ge__ (大于或等于)
print('b'.__ge__('a'))
# __gt__(大于)
print('b'.__gt__('a'))
# __len__(返回字符串长度)
print('abc'.__len__())

# __le__（小于或等于）
print('b'.__le__('a'))
# __lt__（小于）
print('b'.__lt__('a'))
# __str__(返回自已)
print('abc'.__str__())
# capitalize(首字母大写)
s = 'tom'
print(s.capitalize())
# casefold（大写转换成小写）
s = 'TOM'
print(s.casefold())
# center (指定长度和填充字符，内容居中，填充字符留空则为空格)
print(s.center(20))
print(s.center(20, '-'))
# count(计算某个字符串出现的个数，第二个参数：起始位置，第三个参数：结束位置)
s = 'aabbbcccccdd'
print(s.count('cc', 3, 11))
# encode（编码）
s = "中文"
print(s.encode('gbk'))
# endswith（判断字符串是否以某个字符或字符串结尾的，第二个参数：起始位置，第三个参数：结束位置）
s = 'Projects'
print(s.endswith('ts'))
print(s.endswith('e', 0, 5))
# expandtabs（把1个tab键转换成7个空格）
s = 'H\ti'
print(s.expandtabs())
# find（查找某个字符或字符串的索引位置，第二个参数：起始位置，第三个参数：结束位置）
s = 'Hello'
print(s.find('o'))
print(s.find('o', 0, 3))  # 找不到返回-1

# format(字符串格式化/拼接)
name = 'Tom'
age = 18
s = '{0}\'s age is {1}'.format(name, age)
print(s)

s1 = '{name}\'s age is {age}'
result = s1.format(age=18, name='Tom')
print(result)

# index（查找某个字符或字符串的索引位置，和find不一样是，如果字符不存在，会报错）
s = 'Hello'
print(s.index('o'))
print(s.index('e', 0, 3))

# join(将序列中的元素以指定的字符连接生成一个新的字符串)
s = ['H', 'e', 'l', 'l', 'o']
print(''.join(s))
print('-'.join(s))
# ljust(指定长度和填充字符，内容左对齐，填充字符留空则为空格)
s = 'Hello'
print(s.ljust(10, '-'))
# lstrip(移除字符串左侧指定的字符，默认为空格)
s = '   Tom'
print(s.lstrip())

# maketrans(创建字符映射的转换表，配合translate函数使用)
intab = "abcde"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
s2 = "Hello abc"
print(s2.translate(trantab))    # H5llo 123

# partition(指定分隔符，将字符串进行分割)
s = 'IamTom'
print(s.partition('am'))
# replace(把字符串中的old(旧字符串)替换成new(新字符串),如果指定第三个参数max，则替换不超过max次)
s = 'Tom'
print(s.replace('m', 'o'))
# rfind(从右边查找指定字符串出现的位置，如果没有匹配项则返回-1)
s = 'one two one'
print(s.rfind('one'))
print(s.rfind('one', 0, 6))  # 指定起始和结束位置
# rjust(指定长度和填充字符，内容右对齐，填充字符留空则为空格)
s = 'Hello'
print(s.rjust(10, '-'))
# rpartition（ 指定分隔符，从右边开始将字符串进行分割）
s = 'IamTom_IamTom'
print(s.rpartition('am'))
# split(指定分隔符对字符串进行切片，如果指定第二个参数num，则只分隔num次，最后返回一个列表)
s = 'a b c d'
print(s.split())
print(s.split(' ', 2))  # 从左边开始，按空格分隔两次
# rsplit(指定分隔符对字符串进行切片，如果指定第二个参数num，则只分隔num次，最后返回一个列表)
s = 'a b c d'
print(s.rsplit())
print(s.rsplit(' ', 2))  # 从右边开始，按空格分隔两次
# rstrip(删除字符串末尾的指定字符，默认为空格)
s = '!!! I am Tom !!!'
print(s.rstrip('!'))

# splitlines(按换行符来分隔字符串，返回一个列表)
s = 'a\nb\nc'
print(s.splitlines())    # 默认参数为False
print(s.splitlines(True))  # 指定Ture参数，则保留换行符
# startswith（判断字符串是否以某个字符或字符串开头的，第二个参数：起始位置，第三个参数：结束位置）
s = 'Projects'
print(s.startswith('Pr'))
print(s.startswith('e', 4, 8))
# strip(删除字符串前后的指定字符，默认为空格)
s = '!!! I am Tom !!!'
print(s.strip('!'))
print(s.strip('!').strip())
# swapcase（大小写互换）
s = 'I am Tom'
print(s.swapcase())
# title(转换成标题，就是每个单词首字母大写)
s = 'i am tom'
print(s.title())
# zfill(指定字符串的长度。原字符串右对齐，前面填充0)
s = 'Hello'
print(s.zfill(10))
