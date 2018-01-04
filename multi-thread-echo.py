#!/usr/bin/python

import socket
import multiprocessing


def worker(boundSocket, num):
	print "Worker #%d Waiting for client..." % (num)
	(client, (ip, port)) = boundSocket.accept()
	print "Client connected!" 
	print "ip: ", ip
	print "port:", port
	
	print "Starting ECHO server with client #%d" % (num)
	
	# data has to be "something" for the while loop to work
	data = 'dummy'
	# while client still sends data
	while len(data):
		# receives data from the client
		data = client.recv(2048)
		print "Client #%d sent: %s" % (num,data)
		# sends the same data back to the client
		client.send(data)
	print "Worker #%d Closing connection..." % (num)
	client.close()

# Address Family   Reliability Option (TCP), SOCK_DGRAM (UDP)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket option that allows quick reuse of interface/port pairings
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Interface to listen on, port number (as a tuple)
tcpSocket.bind(("0.0.0.0", 8000))

# Max number of concurrent connections
tcpSocket.listen(2)


"""
for x in data:
	client.send((str(x)+"\n"))
"""
if __name__ == '__main__':
	client_1 = multiprocessing.Process(target=worker, args=(tcpSocket, 1,))
	client_1.start()
	client_2 = multiprocessing.Process(target=worker, args=(tcpSocket, 2,))
	client_2.start()



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


"""
print "Waiting for client..."
# accept() is a blocking call - will wait until a client connects
(client, (ip, port)) = tcpSocket.accept()
"""
