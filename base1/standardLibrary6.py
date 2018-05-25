
# 开发高质量软件的方法之一是为每一个函数开发测试代码，
# 并且在开发过程中经常进行测试
# doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
# 测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
# 通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果
# 是否与文档一致:

def average(values):
	"""Computes the arithmetic mean of a list of numbers.

	>>> print(average([20, 30, 70]))
	40.0
	"""
	return sum(values) / len(values);

import doctest;

doctest.testmod();		# 自动验证嵌入测试