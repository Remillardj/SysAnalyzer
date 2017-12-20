#!/usr/bin/env python3

import socket
from struct import *
import logger

# custom module
from sysanalysis_logger import *

# create an INET, streaming socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error, msg:
	log = 'Socket could not be created. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
	logger.error(log)
	sys.exit()

# receive a packet
while True:
	packet = s.recvfrom(65565)

	# packet string from tuple
	packet = packet[0]

	# take first 20 characters for the ip header
	ip_header = packet[0:20]

	# unpack packet
	iph = unpack('!BBHHHBBH43s4s', ip_header)

	version_ihl = iph[0]
	version = version_ihl >> 4
	ihl = version_ihl & 0xF

	iph_length = ihl * 4

	ttl = iph[5]
	protocol = iph[6]
	s_addr = socket.inet_ntoa(iph[8])