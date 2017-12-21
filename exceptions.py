#!/usr/bin/python

try:
	a = 0/1
except:
	print "Exception: Divide by zero"
else:
	print "No exception"
finally:
	print "Cleanup code"


try:
	a = 0/0
except ZeroDivisionError:
	print "Divide by zero"
except:
	print "Unknown error"
	

try:
	a = 0/0
except Exception as im:
	print (dir(im))
	
