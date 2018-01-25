#!/usr/bin/python

# Can use ls(<protocol name>) to find options for the various protocols
# conf will show options for scapy itself (like changing the prompt or setting promiscuous mode)
# lsc() will list commands that can be run in the scapy interpreter

# sniff() encapsulates all the previous work we did with the raw sockets
# It is a blocking call that will return after the conditions are met in the function call
# Supports BPF syntax 
#	pkts = sniff(iface="ens33", count = 3
#	pkts = sniff(iface="ens33", filter="icmp", count = 3)
#

#	pkts[0] displays all contents of the packet in list fashion
#	pkts[0].show() outputs contents based on packet header
#	hexdump(pkts[1]) will output the hex and converted ascii of the packet
#	wrpcap("filename.pcap", pkts) will output the packets sniffed to a pcap
#	read_pkts = rdpcap("filename") will input the pcap into a packets list
