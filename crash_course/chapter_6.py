#!/usr/bin/python

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'bob', 'kevin', 'lyle', 'brad']



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
