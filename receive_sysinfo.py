import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSocket.bind(addr)

while True:
	(data, addr) = UDPSock,recvfrom(buf)
	f = open('sysinfo.txt', 'w')
	f.write(data)
	f.close()
	if (data == 'exit'):
		break
UDPSock.close()
os._exit(0)