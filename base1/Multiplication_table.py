
# 九九乘法表

for i in range(1, 10):
	for j in range(1, i + 1):
		print("{}*{}={}\t".format(i, j, i * j), end = " ");
	print();
print();
	
class multiplicationTable():
	def paint(self, n = 9):
		for row in range(1, n+ 1):
			for col in range(1, row + 1):
				print("{1}*{0}={2}".format(row, col, row * col), end = " ");
			print();
print();

table = multiplicationTable();
table.paint();
print();
table.paint(5);