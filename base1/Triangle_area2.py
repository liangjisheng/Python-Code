
while True :
	triangle = input("输入三角形三边(如10,6,8): ");
	sides = [int(side) for side in triangle.split(",")];
	a, b, c = sides;
	
	# 判断输入的三角形是否合法
	if a + b > c and a + c > b and b + c > a :
		s = a * b * (1-((a**2 + b**2 - c**2)/(2*a*b))**2) ** 0.5
		print('三角形({0[0]},{0[1]},{0[2]})的面积是：{1}'.format(sides,s));
		break;
	else : 
		print("三角形不合法");