#!/usr/bin/python

import signal

def ctrlc_handler(signum, frm):
	print "Haha! You cannot kill me"
	
	
print "Installing signal handler..."
	
signal.signal(signal.SIGKILL, ctrlc_handler)

print "Done!"

while True:
	pass
