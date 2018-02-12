#!/usr/bin/python

import hashlib
import csv
"""

fo = open("real_targets.csv", "r")

md5_list = []



for line in fo.readlines():
	temp = line.strip('\n')
	md5_list.append(hashlib.md5(temp).hexdigest())
	
	
fo.close()
fo = open("email_md5_list_2.txt", "w")

for md5 in md5_list:
	fo.write(md5)
	
fo.close()
	
"""

with open ('real_targets.csv", 'rb') as csvfile:
