#!/usr/bin/env python
#coding:utf8

from socket import socket
s = socket()
s.bind(('192.168.2.181',5200))
s.listen(10)
conn,addr = s.accept()
print "connect with address:%s, port:%s" % addr 
while True:
    data = conn.recv(1024)
    open('upload.txt','w').write(data)
    conn.send('upload ok!')




