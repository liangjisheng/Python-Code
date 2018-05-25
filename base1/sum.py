
num1 = input("输入第一个数字: ");
num2 = input("输入第二个数字: ");

res = float(num1) + float(num2);

print("数字{0}和{1}相加结果为: {2}".format(num1, num2, res));

# 将上面的两行代码合并为一行
print("两数之和为: %.1f" %(float(input("输入第一个数字：")) + float(input("输入第二个数字："))));
