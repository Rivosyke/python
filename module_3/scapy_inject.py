#!/usr/bin/python

#	Simple packet crafting
# 		pkt = IP(dst="google.com")/ICMP()/"I was here"
#	
#	Packet transmission:
#		Layer 2
#		- sendp (layer 2 sending - needs to have many options defined)
#			- Needs to have the interface defined explicitely 
#			- Can do looping to continuously send packets
#				- use "inter" to define an interval in seconds
#		- srp()
#		- srp1()
#			
#
#		Layer 3
#		- send (layer 3 sending - uses local route table) 
#		- sr()
#			- returns answers and unanswered packets
#		- sr1()
#			- returns only answer or sent packets


#		Routing
#		- conf.route - shows the existing route table
#		- conf.route.add(host="x", gw="x") - can also use "net" instead of "host"
#		- conf.route/resync() - sets the "local" route table back to the global table

#		Examples:
#		sr(IP(dst="google.com"), timeout=5) - waits for 5 seconds before timing out
#			- will get 1 unanswered

#		sr1


from scapy.all import *
import socket
import fcntl
from netaddr import IPNetwork


def get_subnet(iface):
	return socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 
										35099, struct.pack('256s', iface))[20:24])


def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

def get_full_info(ip, mask):
	return str(IPNetwork(ip + "/" + mask).cidr)

iface = "ens33"
    
local_ip = get_ip()
local_subnet = get_subnet(iface)
print get_full_info(local_ip, local_subnet)
