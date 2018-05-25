
# 检查python有效标识符的小脚本，python标识符必须以字母或下划线开头
# 后面跟字母、下划线或者数字

import string;

alphas = string.ascii_letters + '_';
nums = string.digits;

print("Welcome to the Identifier Checker v1.0");
print("Testees must be at least 2 chars long");

myinput = input("Identifier to test?");

if len(myinput) > 1:
	if myinput[0] not in alphas:
		print("invalid: first symbol must be alphabetic");
	else:
		for otherChar in myinput[1:]:
			if otherChar not in alphas + nums:
				print("invalid: remaining symbols must be alphabetic");
				break;
		else:
			print("okay as an identifier");