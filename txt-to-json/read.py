#!/usr/bin/python3

import json

f = open("hello.txt")
line = f.readline()
line=line.strip('\n')
dictTest = {}
value = []

while line:
    key = line
    print("key", key)
    line = f.readline()
    line=line.strip('\n')
    while "*" not in line:
        if line != "":
            value.append(line)
        line = f.readline()
        line=line.strip('\n')
    
    dictTest[key] = value
    if "*" in line:
        line = f.readline()
        line = f.readline()
        line=line.strip('\n')

f.close()
print(dictTest)



# python2json = {}
# listData = [1,2,3]
# python2json["listData"] = listData
# python2json["strData"] = "test python obj 2 json"

# #转换成json字符串
# json_str = json.dumps(python2json)
# print(json_str)