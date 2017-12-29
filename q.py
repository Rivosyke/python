#!/usr/bin/python

import threading
import Queue
import time

class WorkerThread(threading.Thread):
	def __init__ (self, queue, ID):
		threading.Thread.__init__(self)
		self.queue = queue
		self.ID = ID
		
	def run(self):
		print "In WorkerThread"
		while True:
			counter = self.queue.get()
			print "Worker #%d - Ordered to sleep for %d seconds!" % (self.ID, counter)
			time.sleep(counter)
			print "Worker #%d - Finished sleeping for %d seconds!" % (qqself.ID, counter)
			self.queue.task_done()



queue = Queue.Queue()


for i in range(10):
	print "Creating WorkerThread : %d" % i
	worker = WorkerThread(queue, i)
	worker.setDaemon(True)
	worker.start()
	print "WorkerThread %d Created!" % i
	
for j in range (10) :
	queue.put(j)
	
queue.join()

print "All tasks done"
