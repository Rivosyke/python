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
"""

import os

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

def Menu():
	cls()
	

"""
raw_text = ""
try:
	with open("alice.txt") as fo:
		raw_text = fo.read()
except IOError:
	print ("Can't open as the file can't be found!")
else:
	words = raw_text.split()
	words = [x.rstrip() for x in words]
	words = [x.lower() for x in words]
	#print "Approximate amount of words: " + str(len(words))

word_count = {}
for word in words:
	if word in word_count:
		word_count[word] +=1
	else:
		word_count[word] = 1

# This will return a list of keys that have been sorted by their values
high_values = sorted(word_count, key=word_count.__getitem__, reverse=True)

for word in high_values[:10]:
	print word + ":\t " + str(word_count[word])
"""

import json

def get_stored_username():
	""" Get Stored Name"""
	filename = 'username.json'
	try:
		with open(filename) as fo:
			username = json.load(fo)
	except IOError:
		return None
	else:
		return username
		
		
def get_new_username():
	username = raw_input("What is your name? ")
	filename = 'username.json'
	with open (filename, 'w') as fo:
		json.dump(username, fo)		
	return username
	
def yes_no(prompt):
	print prompt,
	answer = raw_input("(y/n) ")
	if answer == 'y':
		return 1
	else:
		return 0
		
		
		
def greet_user():
	username = get_stored_username()
	if username:
		if yes_no("Is " + username + " the correct user? "):
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")
			
greet_user()







