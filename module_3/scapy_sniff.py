#!/usr/bin/python

# https://stackoverflow.com/questions/23269226/scapy-in-a-script
# Can use ls(<protocol name>) to find options for the various protocols
# conf will show options for scapy itself (like changing the prompt or setting promiscuous mode)
# lsc() will list commands that can be run in the scapy interpreter

# sniff() encapsulates all the previous work we did with the raw sockets
# It is a blocking call that will return after the conditions are met in the function call
# Supports BPF syntax 
#	pkts = sniff(iface="ens33", count = 3
#	pkts = sniff(iface="ens33", filter="icmp", count = 3)
#

#	pkts will show a count of the type of packets in the list (TCP, UDP, ICMP, other)
#	pkts[0] displays all contents of the packet in list fashion
#	pkts[0].show() outputs contents based on packet header
#	hexdump(pkts[1]) will output the hex and converted ascii of the packet

# 	Writing PCAP:
#		wrpcap("filename.pcap", pkts) will output the packets sniffed to a pcap
# 	Reading PCAP:
#		read_pkts = rdpcap("filename") will input the pcap into a packets list

#	Print packets as they come in:
#		(iface='ens33', filter='icmp', count=30, prn=lambda x: x.summary())
#
#	Export packet as string:
#		export_pkt = str(pkts[0])
#	Reconstruct ether frame of the packet:
#		recon = Ether(export_pkt) - 
#
#	Convert exported packet into base64:
#		b64_pkt = export_object(export_pkt)
#	Converting back into packet object:
#		newPkt = import_object()
#			<paste in base64 code> <hit control-d>
#			<use Ether on newPkt to reconstruct>

# Create a packet sniffer with Scapy for HTTP protocol and print summary
#	- print http headers
#	- data in GET/POST

# Create Wi-Fi sniffer and print out SSIDs in your area by analyzing beacon frames

from scapy.all import *

count = 0

pkts = sniff(filter='port 8000', count=30)

for pkt in pkts:
	if pkt.haslayer(Raw):
		if pkt[Raw].load.__contains__('User-Agent'):
			print "Pkt count: " + str(count)
			print pkt[Raw].load



