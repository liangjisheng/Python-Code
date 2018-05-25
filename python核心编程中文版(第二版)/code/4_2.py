
a, b = -4, 12;
# print(cmp(a, b));

# str()函数得到的字符串可读性好，而repr()函数得到的字符串通常可以用来重新
# 获得改对象，通常情况下obj == eval(repr(obj))这个等式是成立的
# str() 致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于
# eval()求值， 但很适合用于 print 语句输出

print(str(4.53-2j));
print(str(1));
print(str(2e10));
print(str([0, 5, 9, 9]));
print(repr([0, 5, 9, 9]));
# print(`[0, 5, 9, 9]`);
print();

class Foo:
	pass;

class Bar(object):
	pass;

print(type(''));
print(type('xyz'));
print(type(100));
print(type(0+0j));
print(type(0.0));
print(type([]));
print(type( () ));
print(type({}));
print(type(type));
print();

foo = Foo();
bar = Bar();
print(type(Foo));
print(type(foo));
print(type(Bar));
print(type(bar));