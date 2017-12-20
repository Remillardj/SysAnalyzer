#!/usr/bin/env python3

from sysinfo import *

import os
from socket import *
host = "192.168.56.2"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCKDGRAM)
while True:
	data = sysinfo()
	UDPSock.sendto(data, addr)
	if (data == 'exit'):
		break
UDPSock.close()
os._exit(0)