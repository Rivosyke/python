#!/usr/bin/python

import SocketServer
import socket

# This is the working function of what the server does when a client connects
class EchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
			print "Got conn from:", self.client_address
			data = "dummy"
			
			while len(data):
				data = self.request.recv(1024)
				print "Client sent: " + data
				self.request.send(data)
				
			print "Client left"
			
			
			
			
serverAddr = ("0.0.0.0", 9000)

# Pass in a tuple that it binds to and a object representing the handler / worker
server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever()
