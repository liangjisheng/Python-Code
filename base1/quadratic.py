
# 二次方程(quadratic equation)的计算

# ax**2 + bx + c = 0;
# a, b, c 用户提供

import cmath;

a = float(input("输入a: "));
b = float(input("输入b: "));
c = float(input("输入c: "));

# 计算delta
delta = (b ** 2) - (4 * a * c);

# 二次方程的两个解
sol1 = (-b - cmath.sqrt(delta)) / (2 * a);
sol2 = (-b + cmath.sqrt(delta)) / (2 * a);

print("结果为 {0} 和 {1}".format(sol1, sol2));