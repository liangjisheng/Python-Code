
# test

x = (int)(input("please input math record: "));

if x >= 60:
	if x >= 70:
		if x >= 80:
			if x >= 90:
				print("Best");
			else:
				print("Excellent");
		else:
			print("Good");
	else:
		print("Just Pass");
else:
	print("No Pass");
	
print();

if x >= 90:
	print("Best");
elif x >= 80:
	print("Excellent");
elif x >= 70:
	print("Good");
elif x >= 60:
	print("Just Pass");
else:
	print("No Pass");