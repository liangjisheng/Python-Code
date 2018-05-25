
# exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，
# exec可以执行更复杂的 Python 代码

exec('print("hello world")');
exec("print('runoob.com')");

x = 10;
expr = """
z = 30;
sum = x + y + z;
print(sum);
"""

# exec(expr);

def func():
    y = 20
    exec(expr);
    exec(expr, {'x': 1, 'y': 2});
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4});
    
func();

# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系
# isinstance() 会认为子类是一种父类类型，考虑继承关系
a = 2;
print(isinstance(a, int));
print(isinstance(a, str));
print(isinstance(a, (str, int, list)));	# 是元组中的一个返回True
print();

class A:
	pass;

class B(A):
	pass;
	
print(isinstance(A(), A));		# True
print(type(A()) == A);			# True
print(isinstance(B(), A));		# True
print(type(B()) == A);			# False