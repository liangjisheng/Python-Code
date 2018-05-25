
import random;

x = random.choice(range(100));
y = random.choice(range(200));

if x > y :
	print("x: ", x);
elif x == y :
	print("x + y: ", x + y);
else : 
	print("y: ", y);
	
input();