#!/usr/bin/python3

f = open("hello.txt")
line = f.readline()
while line:
    line=line.strip('\n')
    print(line)
    line = f.readline()