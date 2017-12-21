#!/usr/bin/python

names = ['john', 'ryan', 'andy', 'notbill']

for x in names:
	if x == 'bill':
		print "Found bill!"
		break
else:
	print "Name not found..."	


print (range(10,0,-1))


for item in range(0,10,1):
	print item
