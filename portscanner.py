#Python port scanner

import socket
import keyboard
import subprocess
import sys
from datetime import datetime

#Prints infoprmation about open ports
def print_port(port):
	if port == 20:
		print("Port 20:FTP    		Open")
	if port == 21:
		print("Port 21:FTP    		Open")
	if port == 22:
		print("Port 22:SSH    		Open")
	if port == 23:
		print("Port 23:Telnet 		Open")
	if port == 25:
		print("Port 25:SMTP   		Open")
	if port == 53:
		print("Port 53:DNS    		Open")
	if port == 67:
		print("Port 67:DHCP   		Open")
	if port == 68:
		print("Port 68:DHCP   		Open")
	if port == 69:
		print("Port 69:TFTP   		Open")
	if port == 80:
		print("Port 80:HTTP   		Open")
	if port == 110:
		print("Port 110:POPv3 		Open")
	if port == 123:
		print("Port 123:NTP   		Open")
	if port == 137:
		print("Port 137:NetBIOS		Open")
	if port == 138:
		print("Port 138:NetBIOS   	Open")
	if port == 139:
		print("Port 139:NetBIOS   	Open")
	if port == 143:
		print("Port 143:IMAP	   	Open")
	if port == 161:
		print("Port 161:SNMP	   	Open")
	if port == 162:
		print("Port 162:SNMP	   	Open")
	if port == 179:
		print("Port 179:BGP		   	Open")
	if port == 389:
		print("Port 389:LDAP	   	Open")
	if port == 443:
		print("Port 443:HTTPS   	Open")
	if port == 636:
		print("Port 636:LDAPS   	Open")
	if port == 989:
		print("Port 989:SFTP	   	Open")
	if port == 990:
		print("Port 139:SFTP	   	Open")


#Clears the screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
subprocess.call('clear', shell=True)
#Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

#Check what time the scan started
t1 = datetime.now()

#Using the range function to specify ports (here it will scan all ports between 1 and 1024)
try:
	for port in range(1, 1025):
		sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		resultTCP = sockTCP.connect_ex((remoteServerIP, port))
		sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		resultUDP = sockUDP.connect_ex((remoteServerIP, port))
		if ((resultTCP or resultUDP) == 0):
			print_port(port)
		sockTCP.close()
		sockUDP.close()

#Some error handling
except KeyboardInterrupt:
	print("You pressed Ctrl+C")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()

#Checking the time again
t2 = datetime.now()

#Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

#Print the information to the screen
print("Scan completed in: ", total)