
from string import Template;

# 新的字符串模板的优势是不用去记住所有的相关细节，而是像现在shell风格的脚本
# 语言里面那样使用美元符号$
s = Template("There are ${howmany} ${lang} Quotation Symbols");
print(s.substitute(lang = "python", howmany = 3));

# substitute在key缺少的情况下会报一个keyError异常出来
# print(s.substitute(lang = "python"));

print(s.safe_substitute(lang = "python"));
print();

print("\\n");
print(r'\n');

s = "foobar";
for i, t in enumerate(s):
	print(i, t);
print();

s, t = 'foa', 'obr';
print(zip(s, t));
print(list(zip(s, t)));

print(isinstance(u'\0xAB', str));
print(isinstance('\0xAB', str));
# python3中没有unicode，所有的字符编码都统一成unicode
# print(not isinstance('foo', unicode));

print(chr(65));
print(ord('a'));

quest = 'what is your favorite color?';

# 将字符串的第一个字母大写
print(quest.capitalize());
print(quest.center(40));
print(quest.count('or'));
print(quest.endswith('blue'));
print(quest.endswith('color?'));
print(quest.find('or', 30));
print(quest.find('or', 22));
print(quest.find('or', 10));
print(':'.join(quest.split()));
print(quest.replace('favorite color', 'quest'));
print(quest.upper());