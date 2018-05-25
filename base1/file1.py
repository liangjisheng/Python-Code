
# 文件操作

# write
with open("test.txt", "wt") as out_file:
	out_file.write("asdf\ntest");
	
# read
with open("test.txt", "rt") as in_file:
	text = in_file.read();