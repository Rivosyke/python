#!/usr/bin/python

import os

fo = open("kern.log.1", "r")
fw = open("results.txt", "w")

for line in fo.readlines():
	if (line.__contains__("USB")or (line.__contains__("usb"))):
		fw.write(line)

fw.close()
fo.close()

