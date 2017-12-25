#!/usr/bin/python

import os

#print os.getcwd()

#os.mkdir("temp")


#exercise to start at the root and navigate through a predetermined list
#of words
#chdir(path)
#listdir(path)
#os.path.isfile()
#os.path.isdir()

#for item in glob.glob(os.path.join(".", "*")):

target = '/home/rivo/Gits/python'
target_list = ['home', 'rivo', 'Gits', 'python']
os.chdir("/")




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
	
	
	
		
		



