#!/usr/bin/python
"""
def city_country(city, country):
	return city.title() + ", " + country.title()

	
prompt_city = "Enter city name: "
prompt_country = "Enter country name: "

count = 0

while count < 3:
	city = raw_input(prompt_city)
	country = raw_input(prompt_country)
	
	print city_country(city, country)
	count+=1
"""
"""
def make_album(artist, album, tracks = ''):
	if tracks:
		return {'artist':artist, 'album':album, 'tracks':tracks}
	else:
		return {'artist':artist, 'album':album}
	
prompt_artist = "Ente artist name: "
prompt_album = "Enter album name: "
prompt_tracks = "Enter # of tracks: "
count = 0

album_list=[]

while count < 3:
	artist = raw_input(prompt_artist)
	album = raw_input(prompt_album)
	tracks = int(raw_input(prompt_tracks))
	
	if tracks > 0:
		album_list.append(make_album(artist, album, tracks))
	else:
		album_list.append(make_album(artist, album))
	count+=1

for album in album_list:
	if album.__len__() > 2:
		print "Artist: " + album['artist'].title()
		print "Album: " + album['album'].title()
		print "Tracks: " + str(album['tracks'])
	else:
		print "Artist: " + album['artist'].title()
		print "Album: " + album['album'].title()
		
	
	
"""

