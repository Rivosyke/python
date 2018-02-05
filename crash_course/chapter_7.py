#!/usr/bin/python

responses = {}

polling = True

while polling:

	name = raw_input("What is your name? ")
	
	response = raw_input("Mountain? ")
	
	responses[name] = response
	
	repeat = raw_input ("Continue? ")
	
	if repeat.lower() == 'no':
		polling = False

print "--- Results ---"

for name, response in responses.items():
	print name + " wants to climb " + response
