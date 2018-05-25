
print("求一元二次方程的根");

import cmath;
import math;

a = float(input("a 的值: "));
b = float(input("b 的值: "));
c = float(input("c 的值: "));

delta = b ** 2 - 4 * a * c;

print("delta的值: {0}".format(delta));

if 0 == delta:
	x = -b / (2 * a);
	print("x 的值为{0}".format(x));
elif delta > 0 :
	x1 = (-b + math.sqrt(delta)) / (2 * a);
	x2 = (-b - math.sqrt(delta)) / (2 * a);
	print("x1的值为{0}, x2的值为{1}".format(x1, x2));
else:
	x1 = (-b + cmath.sqrt(delta)) / (2 * a);
	x2 = (-b - cmath.sqrt(delta)) / (2 * a);
	print("x1的值为{0}, x2的值为{1}".format(x1, x2));