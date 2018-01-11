#!/usr/bin/python

import socket
import struct

#socket.socket(family, type, proto)

ARP_packet = 0x0806
IP_packet = 0x0800
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(ARP_packet))

ethr_src = '\xfe\x80\x34\x92\x89\x7f'
ethr_dst = '\x00\x50\x56\xC0\x00\x08'

ethr_typ = '\x08\x06'

arp_hw_typ = '\x00\x01'
arp_proto_typ = '\x08\x00'
arp_hw_len = '\x06'
arp_proto_len = '\x04'
arp_opcode = '\x00\x01'
arp_eth_src = ethr_src
arp_eth_dst = ethr_dst
arp_ip_src = '\xc0\xa8\x6f\x80'
arp_ip_dst = '\xc0\xa8\x6f\x45'

ethr_frame_pack = '!6s6s2s'
arp_frame_pack = '!2s2sss2s6s4s6s4s'
full_frame_pack = (ethr_frame_pack + arp_frame_pack)


rawSocket.bind(("ens33", socket.htons(ARP_packet)))

ethr_frame = struct.pack(ethr_frame_pack, ethr_dst, ethr_src, ethr_typ)
arp_frame = struct.pack(full_frame_pack, arp_hw_typ, arp_proto_typ, 
						arp_hw_len, arp_proto_len, arp_opcode,
						arp_eth_src, arp_ip_src, arp_eth_dst, arp_ip_dst)

packet = ethr_frame + arp_frame

#rawSocket.send(packet + "Hello there!")




