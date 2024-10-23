#Test script to see if we can communicate with RobotStudio on a local machine
#Times how long it takes to form the connection and recieve an acknowledgement

#Have to open the RAPID socket first - then connect

import socket
import time

print("Connecting to Socket")

#Open the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the local socket
sock.connect(('127.0.0.1', 55555))

#Send a message and start the timer

start_time = time.time()
sock.send(bytes("ECHO:Hello world", 'UTF-8'))

#Print the response from the socket
print(sock.recv(4096).decode('UTF-8'))
fin_time = time.time() - start_time

# Wait till user press 'Enter' to exit
input(f"Comms took: {fin_time}, Press Enter to continue...")







#Send a message
sock.send(bytes("CLOS:1", 'UTF-8'))

#Print the response from the socket
print(sock.recv(4096).decode('UTF-8'))
