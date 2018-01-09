#!/usr/bin/python

import socket 
import struct
import binascii


# look up IP protocol HEX definition in /usr/include/linux/if_ether.h
protocol_type = 0x0800

#socket.socket(family, type, proto)
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(protocol_type))
"""
pkt = rawSocket.recvfrom(2048)

# Start parsing of Ethernet header
ethernetHeader = pkt[0][0:14]

# The ! represents "Network Byte Order"
eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)

binascii.hexlify(eth_hdr[0])

binascii.hexlify(eth_hdr[1])

binascii.hexlify(eth_hdr[2])

# Start parsing of IP header
ipHeader = pkt[0][14:34]

ip_hdr = struct.unpack("!12s4s4s", ipHeader)

print "Source IP address:  " + socket.inet_ntoa(ip_hdr[1])

print "Destination IP address:  " + socket.inet_ntoa(ip_hdr[2])

#initial part of the tcp header

tcpHeader = pkt[0][34:54]

tcp_hdr = struct.unpack("!HH16s", tcpHeader)
"""
while True:
	dashes = "---- "
	pkt = rawSocket.recvfrom(2048)
	if struct.unpack("!9sb10s", pkt[0][14:34])[1] == 6:
		# Print Source/Dest IPs
		ipHeader = pkt[0][14:34]
		ip_hdr = struct.unpack("!12s4s4s", ipHeader)
		print "Source IP address:  " + socket.inet_ntoa(ip_hdr[1])
		print "Dest IP address:  " + socket.inet_ntoa(ip_hdr[2])
				
		# Print TCP Info
		tcpHeader = pkt[0][34:54]
		tcp_hdr = struct.unpack("!HHII8s", tcpHeader)
		print dashes + "Source Port:\t" + str(tcp_hdr[0])
		print dashes + "Destination Port:\t" + str(tcp_hdr[1])
		print dashes + "Sequence Number:\t" + str(tcp_hdr[2])
		print dashes + "Acknow Number:\t" + str(tcp_hdr[3])
	else:
		continue

