
# unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的
# 文件里提供一个更全面的测试集:

import unittest;

def average(values):
	"""Computes the arithmetic mean of a list of numbers.

	>>> print(average([20, 30, 70]))
	40.0
	"""
	return sum(values) / len(values);

class TestStatisticalFunctions(unittest.TestCase):
	def test_average(self):
		self.assertEqual(average([20, 30, 70]), 40.0);
		self.assertEqual(round(average([1, 5, 7]), 1), 4.3);
		self.assertRaises(ZeroDivisionError, average, []);
		self.assertRaises(TypeError, average, 20, 30, 70);
		
unittest.main();	# calling from the command line invokes all test