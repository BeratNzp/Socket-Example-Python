#!/usr/bin/python3
#! -*- encoding: utf-8 -*-
from socket import *
serverIP = "172.31.81.15"
serverPort = 12000
client = socket(AF_INET, SOCK_STREAM)
client.connect((serverIP, serverPort))

message=input(":")
client.send(message.encode())
response=client.recv(4096)
print("[Client] '%s'" % message)
print("[Server] '%s'" % response.decode())
