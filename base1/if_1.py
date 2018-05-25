
number = 7;
guess = -1;
print("数字猜谜游戏");

while guess != number:
	guess = int(input("请你输入你猜的数字: "));
	if guess == number:
		print("ok");
	elif guess < number:
		print("less");
	elif guess > number:
		print("great");

input();