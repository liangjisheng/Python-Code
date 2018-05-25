
# 计算三角形面积

a = float(input("输入三角形的第一边长: "));
b = float(input("输入三角形的第二边长: "));
c = float(input("输入三角形的第三边长: "));

# 计算半周长
s = (a + b + c) / 2;

area = (s * (s - a) * (s - b) * (s - c))  ** 0.5;
print("三角形面积为 %0.2f" %area);