#!/usr/local/bin/python3.7
import socket               # Import socket module

client = socket.socket()         # Create a socket object
host = socket.gethostbyname("")

port = 6813
client.connect((host, port))

print(client.recv(1024))
client.close()