
a = -8.333-1.47j;
print(a);
print(a.real);
print(a.imag);
print(a.conjugate());
print();

# print(coerce(1, 2));
print(divmod(10, 3));
print(divmod(3, 10));
print(divmod(10, 2.5));
print(divmod(2.5, 10));
# print(divmod(2+1j, 0.5-1j));
print();

print(round(3));
print(round(3.45));
print(round(3.4999999));
print(round(3.4999999, 1));

import math;

for eachNum in range(10):
	print(round(math.pi, eachNum));
	
for eachNum in (.2, .7, 1.2, 1.7, -.2, -.7, -1.2, -1.7):
	print("int(%.f)\t%+.f" % (eachNum, float(int(eachNum))));
	print("floor(%.f)\t%+.f" % (eachNum, math.floor(eachNum)));
	print("round(%.f)\t%+.f" % (eachNum, round(eachNum)));
	print('-' * 20);