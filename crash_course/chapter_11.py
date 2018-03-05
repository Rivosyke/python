#!/usr/bin/python

"""
from name_function import get_formatted_name

print ("Enter 'q' at any time to quit.")

while True:
	first = raw_input ("\nFirst Name: ")
	if first == 'q':
		break
	last = raw_input ("Last Name: ")
	if last == 'q':
		break
		
	formatted_name = get_formatted_name(first,last)
	print("\tNeatly formatted name: " + formatted_name + ".")
	
"""

class AnonymousSurvey():
	def __init__self(self, question):
		self.question = question
		self.responses = []
		
	def show_question(self):
		print (self.question)
		
	def store_responses (self, new_response):
		self.responses.append(new_response)
		
	def show_results(self):
		print ("Survey Results: ")
		for response in self.responses:
			print ('- ' + response)
