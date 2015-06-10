#!/usr/bin/env python

import socket
import sys

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

HOST = '192.168.0.19'   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
     
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
         
print 'Socket bind complete'
     
s.listen(10)
print 'Socket now listening'
     
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
        
    while 1:
        data = conn.recv(1024)
        
        if data:
            pw = data.split('power=')[1]
            print pw
            ser.write(pw)      # write a string    
            reply = 'OK... ' + data
            conn.sendall(reply)
             
        if not data: 
            break
            
       
ser.close()             # close port
conn.close()
s.close()
