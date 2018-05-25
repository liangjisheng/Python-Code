
print((1, 2, 3)[1]);
s = "abcdefg";
print("s = %s" % s);
print(s[::-1]);
print(s[::2]);
print(s[-100:100]);
print();

i = -1;
for i in range(-1, -len(s), -1):
	print(s[:i]);
print();

for i in ([None] + list(range(-1, -len(s), -1))):
	print(s[:i]);
	
import string;
print(string.ascii_uppercase);
print(string.ascii_lowercase);
print(string.ascii_letters);
print(string.digits);