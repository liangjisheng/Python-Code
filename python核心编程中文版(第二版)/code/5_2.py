
print(hex(255));
print(hex(230948231));
print(hex(65535 * 2));
print(oct(230948231));
print(oct(65535 * 2));
print();

# ASCII码与其序列值之间的转换
print(ord('a'));
print(ord('A'));
print(ord('0'));
print(chr(97));
print(chr(65));
print(chr(48));
print();

print(bool(1));
print(bool(True));
print(bool(0));
print(bool('1'));
print(bool('0'));
print(bool([]));
print(bool((1,)));
print();

# 无__nonzero__()
class C:
	pass;

c = C();
print(bool(c));
print(bool(C));

# 重载__nonzero__()使它返回False
class C1:
	def __nonzero__(self):
		return False;

c1 = C1();
print(bool(c1));
print(bool(C1));