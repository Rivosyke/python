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


"""
def count_words(filename):
	raw_text = ""
	try:
		with open(filename) as fo:
			raw_text = fo.read()
	except IOError:
		print ("Can't open " + filename + " as the file can't be found!")
	else:
		words = raw_text.split()
		print "Approximate amount of words: " + str(len(words))
		
filenames = ["alice.txt", 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for file in filenames:
	count_words(file)
"""

"""
try:
	num_1 = int(raw_input("Enter Number 1: "))
except ValueError as e:
	print "'" + e.message.split("'")[1] + "'" + " is not a valid number!"
else:
	try:
		num_2 = int(raw_input("Enter Number 2: "))
	except ValueError as e:
		print "'" + e.message.split("'")[1] + "'" + " is not a valid number!"
	else: 
		print "Sum of both numbers is: " + str(num_2 + num_1)
"""

valid = True

while valid:
	num_1 = raw_input("Enter Number 1: ")
	num_2 = raw_input("Enter Number 2: ")
	
	try:
		sum = int(num_1) + int(num_2)
	except ValueError as e:
		print "'" + e.message.split("'")[1] + "'" + " is not a valid number!"
		print "Try again!"
	else:
		print "Sum = " + str(sum)
		valid = False






