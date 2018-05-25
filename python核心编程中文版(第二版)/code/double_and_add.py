
def bits(n):
	"""
	Generates the binary digits of n, start from the least
	significant bit.
	
	bits(151) -> 1, 1, 1, 0, 1, 0, 0, 1
	"""
	while n:
		yield n & 1;
		n >>= 1;
		
def double_and_add(n, x):
	"""
	returns the result of n * x, computed using 
	the double and add algorithm
	"""
	
	result = 0;
	addend = x;
	
	for bit in bits(n):
		if bit == 1:
			result += addend;
		addend *= 2;
	
	return result;

print(double_and_add(151, 1));
print(double_and_add(45645665416313151, 4561554315363546541));