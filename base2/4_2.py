
for food in ("pate", "cheese", "crackers", "yogurt"):
	if food == "yogurt":
		break;
else:
	print("There is no yogurt");
	
# else:仅在循环不是由break语句退出时才会被运行
for food in ("pate", "cheese", "crackers"):
	if food == "yogurt":
		break;
else:
	print("There is no yogurt");

print();

for food in ("pate", "cheese", "rotten apples", "crackers", "whip cream", "tomato soup"):
	if food[0:6] == "rotten":
		continue;
	print("Hey you can %s" % food);
print();

fridge_contents = {"egg":8, "mushroom":20, "pepper":3, "cheese":2};
try:
	if fridge_contents["orange juice"] > 3:
		print("Sure, let's have some juice");
except KeyError:
	print("Awww, there is no juice");
	
try:
	if fridge_contents["orange juice"] > 3:
		print("Sure, let's have some juice");
except KeyError as error:
	print("Awww, there is no %s" %error);
	
# 可以用一个元组包含有关的所有异常类型
try:
	if fridge_contents["orange juice"] > 3:
		print("Sure, let's have some juice");
except (KeyError, TypeError) as error:
	print("Awww, there is no %s" %error);
	
# 处理异常，但希望什么也不做，可以使用pass
try:
	if fridge_contents["orange juice"] > 3:
		print("Sure, let's have some juice");
except KeyError as error:
	#pass;
	print("Awww, there is no %s" %error);
except TypeError:
	pass;
print();
	
# 后面可以跟一个else，try里面的语句没有发生异常是，else里面的语句也被执行
try:
	print("test");
except:
	print("except");
else:
	print("else");