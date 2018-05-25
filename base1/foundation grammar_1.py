#!/usr/bin/python
# A first Python script

import sys		# Load a library module
print(sys.platform);
print(2 * 10);	# 20
print(2 ** 10);	# Raise 2 to a power
x = 'Spam!';
print(x * 8);	# String repetition
print("test");

# python 最具特色的就是使用缩进来表示代码块，不需要使用大括号{}
if True:
	print("True");
else:
	print("False");
	
if True:
	print("Answer ");
	print("True");
else:
	print("Answer ");
	print("False");
print("\n");
	
# python中通常是一行写完一条语句，但如果语句很长，可以使用反斜杠\来实现多行语句
# 类似于C/C++中的宏定义
total = 1 + \
		2 + \
		3;
print(total);
print("\n");

# 在[],{},或()中的多行语句，是不需要反斜杠的
var1 = ["item_one", "item_tow", "item_three", "item_four", "item_five"];
print(var1);

# python中单引号和双引号使用完全相同
# 使用三单引号'''和三双引号"""可以指定一个多行字符串
# 转义符"\"
# 自然字符串，通过在字符串前面加r或R，如r"this is a line with \n",则会显示\n,并不是换行
# python允许处理unicode字符，加前缀u或U，如u"this is an unicode string"
# 字符串是不可变的
# 按字面意义级联字符串,如"this " "is " "string"会被自动转换为"this is string"

word = '字符串';
sentence = "这是一个句子。";
paragraph = """这是一个段落
可以有多行组成""";

print(word);
print(sentence);
print(paragraph);

# 如果在命令行下执行py脚本，则不需要下面的这句话，
# 如果只直接用解释器执行py脚本，为了防止屏幕一闪而过，需要加上这句话，表示输入一行
# input();