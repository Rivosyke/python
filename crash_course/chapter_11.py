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

from survey import AnonymousSurvey

question = "What language did you first learn?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at time to quit.\n")
while True:
	response = raw_input("Language: ")
	if response == 'q':
		break
	my_survey.store_responses(response)
	
print("\nThanks for participating!")
my_survey.show_results()

"""
blah = ['English', 'French', 'English', 'Spanish']

blah.sort()

blah2 = {}
previous = ''

for x in blah:
	if x in blah2.keys():
		blah2[x] += 1
	else:
		blah2[x] = 1
		
values = sorted(blah2, key=blah2.__getitem__, reverse=True)
		
for x in values:
	print x + "\t" + str(blah2[x])
"""	
	
	
	
