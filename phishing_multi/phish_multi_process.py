#!/usr/bin/python

import os
import multiprocessing
import sys

try:
	target_list = open(sys.argv[1], "r")
except IOError:
	print "File error - Unable to open file: " + sys.argv[1]
	print "Exiting..."
	exit()



server_1 = "server_1"
server_2 = "server_2"
server_3 = "server_3"
server_4 = "server_4"

#if __name__ == '__main__':

