#!/usr/bin/python

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'bob', 'kevin', 'lyle', 'brad']



player_status = {}

for player in players:
	player_status[player] = 'dead'
	
for player in player_status:
	print "Player: " + player
	print "Status: " + player_status[player]
