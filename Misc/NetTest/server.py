#!/usr/local/bin/python3.7
import socket

server = socket.socket()
host = '127.0.0.1' #localhost
port = 6813
server.bind((host, port))

server.listen(5)
count = 1
while True:
    c, addr = server.accept()
    print("Connected to ", addr)
    c.send(b"Sup, dork! You are client #" + count.to_bytes())
    c.close()
    count+=1
