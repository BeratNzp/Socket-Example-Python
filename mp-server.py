#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from socket import *
import threading

bindIP = "0.0.0.0"
bindPort = 12000
server = socket(AF_INET, SOCK_STREAM)
server.bind((bindIP, bindPort))
server.listen(5)
print("\r[Server] Listening: %s:%d" % (bindIP, bindPort))

def handleClient(clientSocket):
    request = clientSocket.recv(2048)
    print("[Client] '%s'" % request.decode())
    clientSocket.send("ACK".encode())
    clientSocket.close()

while True:
    client, address = server.accept()
    print("[Client] %s:%d connected." % (address[0], address[1]))
    clientHandler = threading.Thread(target=handleClient,args=(client,))
    clientHandler.start()

clientSocket.close()
