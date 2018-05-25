
print("求一元二次方程的根");
# 二次方程考虑无穷解与无解的情况

# math为简单数学计算模块，cmath为复杂数学计算模块
import cmath;
import math;

a, b, c = input("请输入3个数字(空格分隔): ").split();

a = float(a);
b = float(b);
c = float(c);

delta = (b ** 2) - (4 * a * c);

if 0 == a and 0 == b and 0 == c :
	print("有无穷个解");
elif delta >= 0:
	x1 = (-b - math.sqrt(delta)) / (2 * a);
	x2 = (-b + math.sqrt(delta)) / (2 * a);
	print("结果为: %.2f, %.2f" %(x1, x2));
else:
	print("无解")