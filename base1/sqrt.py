
# 平方根

num = float(input("请输入一个数字: "));
# 这种计算方式要求num必须大于0
num_sqrt = num ** 0.5;
print("%0.3f 的平方根为 %0.3f" %(num, num_sqrt));

# 导入复数数学模块，计算实数和复数平方根
import cmath;

num1 = int(input("请输入一个数字："));
num1_sqrt = cmath.sqrt(num1);
print("{0} 的平方根为 {1:0.3f} + {2:0.3f}j".format(num1, num1_sqrt.real, num1_sqrt.imag));
