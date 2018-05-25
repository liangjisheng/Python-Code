
#/usr/bin/env python

global_str = 'foo';

def foo():
	local_str = 'bar';
	return global_str + local_str;
	
print(foo());

is_this_global = 'xyz';
def foo1():
	global is_this_global;
	this_is_local = 'abc';
	is_this_global = 'def';
	print(this_is_local + is_this_global);
	
foo1();
print(is_this_global);