#!/usr/bin/python

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'bob', 'kevin', 'lyle', 'brad']


"""
player_status = {}

for player in players:
	player_status[player] = 'dead'

for i, player in enumerate(player_status):
	if i % 2 == 0:
		player_status[player] = 'alive'
		
for player in player_status:
	print "Player: " + player
	print "Status: " + player_status[player]


email_recipient = {}

email_recipient['first_name'] = 'bob'
email_recipient['last_name'] = 'sanker'
email_recipient['md5_hash'] = '1A2B3C'
"""

jasper = {'type':'cat', 'owner':'ryan', 'name':'jasper'}
porthos = {'type':'dog', 'owner':'archer', 'name':'porthos'}

pets = [jasper,porthos]

for pet in pets:
	print "Name: " + pet['name'].title()
	print "Type: " + pet['type'].title()
	print "Owner: " + pet['owner'].title()
	

cities = {
	'frankfurt':{
		'country': 'germany',
		'population':'1,000,000',
		'fact':'apfelwein'},
	'los angeles':{
		'country': 'united states',
		'population':'4,000,000',
		'fact':'shitty'},
	'london':{
		'country': 'united kingdom',
		'population': '2,000,000',
		'fact':'warm beer'}
		}
		

for city, attributes in cities.items():
	print "City Name: " + city.title()
	print "\tCountry: " + attributes['country'].title()
	print "\tPopulation: " + attributes['population']
	print "\tFact: " + attributes['fact'].title()





