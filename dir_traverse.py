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
dashes = "----"

def traverse(dirList, dashes):
	if not dirList:
		os.chdir("..")
		return 1
	else:
		cwd = dirList.pop()
		os.chdir(cwd)
		directory.append(dashes + cwd + "\n")
		#print dashes + cwd
		processDir(dashes)
		traverse(dirList, dashes)
		return 0
		
	
def processDir (dashes):
	
	dashes = dashes + "----"
	files = []
	dirs = []
	workingList = os.listdir(".")
	for item in workingList:
		if os.path.isfile(item):
			files.append(item)
		else:
			dirs.append(item)
	
	printFiles(files, dashes)
	while traverse(dirs, dashes) !=1:
		return

	
def printFiles(fileList, dashes):
	for item in fileList:
		directory.append(dashes + item + "\n")
		#print dashes + item

directory = []

startingDashes = ""
processDir(startingDashes)


import socket
# Address Family   Reliability Option (TCP), SOCK_DGRAM (UDP)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket option that allows quick reuse of interface/port pairings
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Interface to listen on, port number (as a tuple)
tcpSocket.bind(("0.0.0.0", 8000))

# Max number of concurrent connections
tcpSocket.listen(2)

print "Waiting for client..."
# accept() is a blocking call - will wait until a client connects
(client, (ip, port)) = tcpSocket.accept()


for x in directory:
	client.send((str(x)))

"""
# data has to be "something" for the while loop to work
data = 'dummy'

# while client still sends data
while len(data):
	# receives data from the client
	data = client.recv(2048)
	print "Client sent: ", data
	# sends the same data back to the client
	client.send(data)
"""
print "Closing connection..."
client.close()

print "Shutting down server..."
tcpSocket.close()
