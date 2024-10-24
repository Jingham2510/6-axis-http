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
input(f"ECHO took: {fin_time}, Press Enter to continue...")


test_pos = ",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,"

start_time = time.time()
sock.send(bytes(f"MVTO:{test_pos}", "UTF-8"))

print(sock.recv(4096).decode("UTF-8"))
fin_time = time.time() - start_time
# Wait till user press 'Enter' to exit
input(f"MVTO took {fin_time} - Press Enter to continue...")

#Send a message
sock.send(bytes("CLOS:1", 'UTF-8'))

#Print the response from the socket
print(sock.recv(4096).decode('UTF-8'))
