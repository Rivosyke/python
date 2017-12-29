#!/usr/bin/python

import os
import thread
import time


def worker_thread(id):
	print "Thread ID %d now alive!" % id
	count = 1
	while True:
		print "Thread with ID %d has counter value %d" % (id, count)
		time.sleep(2)
		count += 1
		
for i in range(5):
	thread.start_new_thread(worker_thread, (i,))
	
print "Main thread going for an infinite wait loop"
while True:
	pass

"""
def child_process():
	print "I am the child process and my PID is: %d" % os.getpid()
	print "The child is exiting"
	
def parent_process():
	print "I am the parent process and my PID is: %d" % os.getpid()
	
	childPID = os.fork()
	
	if childPID == 0:
		# we are inside the child
		child_process()
	else:
		# we are inside the parent process
		print "We are inside the parent process"
		print "Our child has the PID of %d" % childPID
		
	while True:
		pass
		
parent_process()
"""

#os.execvp("ping", ["ping", "127.0.0.1"])
