#!/usr/bin/env python

import socket

s = socket.socket()
s.connect(('192.168.2.181',5200))
while True:
    dat = raw_input('file path:')
    contents = open(dat, 'r').read()
    s.send(contents)
    data = s.recv(1024)
    print data






