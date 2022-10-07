#!/bin/python3

import socket
from IPy import IP
import pyfiglet
import subprocess
import time

subprocess.call('clear', shell=True)

Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)

time.sleep(1)

def scan(target):
	converted_ip = convert_ip(target)
	print('\n' + 'Scanning Target : ' + str(target))
	for port in range(21,500):
		scan_port(converted_ip, port)

def convert_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(s):
	return s.recv(1024)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((ipaddress, port))

		try:
		  banner = get_banner(sock)
		  print('[+] Port' + str(port) + ' is Open ' + ' : ' + str(banner.decode().strip('\n'))) 
		except:
		  print('[+] Port '  + str(port) + ' is Open ')
            
	except:
		pass

if __name__ == "__main__":
	targets = input('[+] Enter Target/s To Scan(for multiple targets use a comma): ')
	if ',' in targets:
		for ip_address in targets.split(','):
			scan(ip_address.strip(' '))
	else:
		scan(targets)
