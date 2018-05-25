
#!/usr/bin/env Python
"readTextFile.py -- read and display test file"

# get filename
fname = input("Ente filename: ");
print();

# attempt to open file for reading
# try里面的语句正常执行的情况下会走else分支，可以在这里面输出文件的内容
try:
	fobj = open(fname, "r");
except IOError as e:
	print("*** file open error:", e);
else:
	# display contents to the screen
	for eachLine in fobj:
		print(eachLine, end = "");
	fobj.close();
	print();