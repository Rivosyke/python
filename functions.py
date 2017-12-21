#!/usr/bin/python

import sys


def print5Times(line_to_print):
	for count in range(0,5):
		print line_to_print
		
		
print5Times(sys.argv[1])
