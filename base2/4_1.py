
a = "Mackintosh apples";
b = "Black Berries";
c = "Golden Delicious apples";

print(a == b);
print(b == c);
print(a[-len("apples"):-1] == c[-len("apples"):-1]);
print();

print("a" > "b");
print("A" > "b");
print("A" > "a");
print("b" > "A");
print("Z" > "a");
print();

print("Zebra" > "aardvark");
print("Zebra" > "Zebrb");
print();

i = 10;
while i > 0:
	print("Lift off in:");
	print(i);
	i = i - 1;
print();

for i in range(10, 0, -1):
	print("T-minus: ");
	print(i);
print();

for i in range(10):
	print(i);