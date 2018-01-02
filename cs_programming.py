#!/usr/bin/python

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


data = ["this", "is", "a", "test"]

for x in data:
	client.send((str(x)+"\n"))

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
