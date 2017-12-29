#!/usr/bin/python

import socket
#                            Address Family   Reliability Option (TCP)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.bind(("0.0.0.0", 8000))
