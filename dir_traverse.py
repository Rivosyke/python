#!/usr/bin/python

import os
import glob
import time
import datetime

#print os.getcwd()

#os.mkdir("temp")


#exercise to start at the root and navigate through a predetermined list
#of words
#chdir(path)
#listdir(path)
#os.path.isfile()
#os.path.isdir()

#for item in glob.glob(os.path.join(".", "*")):

#target = '/home/rivo/Gits/python'
#target_list = ['home', 'rivo', 'Gits', 'python']
#os.chdir("/")
#sets the output format for doing timestamps
time_format = "%Y-%m-%d %H:%M:%S"



startingList = os.listdir(".")
dirList = []
fileList = []
dashes = "----"
print os.getcwd()

for item in startingList:
	if os.path.isfile(item):
		fileList.append(item)
	elif os.path.isdir(item):
		dirList.append(item)

for item in fileList:
	print dashes + item.strip()
	
while not dirList:
	dashes = dashes + dashes
	continue

print dashes
print os.getcwd()
"""
for item in current_list:
	if os.path.isfile(item):
		print item.strip() + "\t\tF"
	elif os.path.isdir(item):
		print item.strip() + "\t\tD"
"""
"""
for item in current_list:
	info = os.stat(item)
	print item
	print "\t" + str(info.st_size)
	info_time = datetime.datetime.utcfromtimestamp(info.st_mtime)
	print "\t" + info_time.strftime(time_format) + "\n"
"""
"""
for item in current_list:
	if os.path.isfile(item):
		print item.strip() + "\t\tF"
	elif os.path.isdir(item):
		print item.strip() + "\t\tD"
"""
"""
for item in glob.glob(os.path.join(".", "*")):
	print item
"""


"""
while (os.getcwd() != target):
	print "Currently in:\t" + os.getcwd()
	cwd = os.getcwd()
	dirList = os.listdir(".")
	
	for item in dirList:
		if item in target_list:
			if cwd == "/":
				cwd = os.getcwd() + item
				os.chdir(cwd)
				break
			else:
				cwd = os.getcwd() + '/' + item
				os.chdir(cwd)
				break

print "Currently in:\t" + os.getcwd()
"""
	
	
	
		
		



