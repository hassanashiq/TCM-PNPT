#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate the host name to IPV4
	
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py")

#a pretty banner
print("-" * 50)
print("Scanning : " + target)
print("Time Started", str(datetime.now()))
print("-" * 50)

try:
	for port in range (130,140):
		print("Testing",port)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
	
		if result == 0:
			print(f"PORT {port} is open")
		s.close()
	
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error():
	print("Could not connect to the server")
	sys.exit()
