#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from socket import * # Import all modules of 'socket' library
import threading # Import 'threading' module

bindIP = "0.0.0.0" # Set Server IP
bindPort = 12000 # Set Server Port
server = socket(AF_INET, SOCK_STREAM) # Create socket with IPv4 & TCP
server.bind((bindIP, bindPort)) # Set IP & Port to Socket
server.listen(5) # How many clients can requests (Max.)(Defualt: 5)
print("\r[Server] Listening: %s:%d" % (bindIP, bindPort)) # Output Example: [Server] Listening: 0.0.0.0:12000

def handleClient(clientSocket): # Create a function for connect
    request = clientSocket.recv(2048) # How many bytes can clients send (Max.)(Default: 2048)
    print("[Client] '%s'" % request.decode()) # Print decodded request of client.
    clientSocket.send("ACK".encode()) # Send a encoded string to client.
    clientSocket.close() # Stop the client.

while True: # Alltime
    client, address = server.accept()
    print("[Client] %s:%d connected." % (address[0], address[1])) # Print IP & Port when a client connect.
    clientHandler = threading.Thread(target=handleClient,args=(client,)) # Receive multiple requests.
    clientHandler.start()

clientSocket.close() # Stop client
