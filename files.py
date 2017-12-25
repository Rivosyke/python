#!/usr/bin/python

import os

fo = open("file.txt", "w")

print fo


for count in range(0,10):
	fo.write(str(count) + "\n")

fo.close()

fo = open("file.txt", "a")

for count in range (10,20):
	fo.write(str(count) + "\n")

fo.close()


fo = open("file.txt", "r")

for line in fo.readlines():
	print line.strip()
	
os.rename("file.txt", "file2.txt")

os.delete("file2.txt")
tes
