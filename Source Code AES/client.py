#!/usr/bin/env python

import random
import socket, select
from time import gmtime, strftime
from random import randint
import time
import os

#image = raw_input("enter the name of the image file: ")

HOST = '127.0.0.1'
PORT = 6662

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)
command = int(input("Masukkan command :\n1.Encrpyt\n2.Decrypt\n"))

try:
    if command==1 :
     # open image
     os.system('python3 enc.py')
     time.sleep(10)
     myfile = open('encrypted.enc', 'rb')
     bytes = myfile.read()
     size = len(bytes)
     sock.send('1')
    elif command==2 :
     # open image
     os.system('python3 dec.py')
     time.sleep(10)
     myfile = open('output.png', 'rb')
     bytes = myfile.read()
     size = len(bytes)
     sock.send('2')

    # send image size to server
    sock.sendall("SIZE %s" % size)
    answer = sock.recv(4096)

    print 'answer = %s' % answer

    # send image to server
    if answer == 'GOT SIZE':
        sock.sendall(bytes)

        # check what server send
        answer = sock.recv(4096)
        print 'answer = %s' % answer

        if answer == 'GOT IMAGE' :
            sock.sendall("BYE BYE ")
            print 'Image successfully send to server'

    myfile.close()

finally:
    sock.close()