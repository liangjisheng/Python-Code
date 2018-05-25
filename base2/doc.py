
# 如果模块、类或函数定义的第一条语句是一个字符串，该字符串就成为了相关对象
# 的文档字符串，通过对象的__doc__属性可以访问文档字符串

def fact(n):
	"This function computes a factorial"
	if n <= 1 : return 1;
	else: return n * fact(n - 1);
	
print(fact.__doc__);