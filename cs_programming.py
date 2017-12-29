#!/usr/bin/python

import socket
# Address Family   Reliability Option (TCP)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Interface to listen on, port number (as a tuple)
tcpSocket.bind(("0.0.0.0", 8000))

# Max number of concurrent connections
tcp.Socket.listen(2)



