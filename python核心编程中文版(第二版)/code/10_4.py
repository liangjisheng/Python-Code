
try:
	float('abc123');
except:
	import sys;
	exc_tuple = sys.exc_info();
	print(exc_tuple);
	for eachItem in exc_tuple:
		print(eachItem);