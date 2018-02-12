#!/usr/bin/python
"""
with open('pi_million_digits.txt') as file_object:
	pi_string = ""
	
	for line in file_object:
		pi_string += line.rstrip()
	
#	print pi_string[:50]
	
	

	birthday = ""
	birthday = raw_input("Birthday in 'ddmmyy' format: ")
	while birthday.lower() != 'q':
		if birthday in pi_string:
			print "Your birthday is in the first million digits of PI!"
		else:
			print "You ain't in there"
			
		birthday = raw_input("Birthday in 'ddmmyy' format: ")
"""

filename = "alice2.txt"
AIW_text = ""

try:
	with open(filename) as AIW_fo:
		AIW_text = AIW_fo.readlines()
except IOError:
	print ("Can't open " + filename + " as the file can't be found!")


