#!/usr/bin/env python

import httplib, urllib, urllib2
import serial
import time
import re
import numpy

ser = serial.Serial('/dev/ttyACM0', 9600)
pattern = re.compile("^\s+|\s*,\s*|\s+$")

resetCount = 2
loopCount = 1
watt = 0

while 1 :
    serialValue = ser.readline() 
    print serialValue    
    splitValues = pattern.split(serialValue)
    watt += float(splitValues[0])

    if(loopCount == resetCount) :
        watt /= loopCount
        
        param = {'watt' : watt, 'power' : splitValues[1]}
        port = 80
        url = 'http://202.30.29.239:%s/update.php?%s' % (port, urllib.urlencode(param))

        #1st
        response = urllib2.urlopen(url)
        html = response.read()

        print html

        #2nd
#       response2, content = httplib2.http().request(url)
        
#       print response2.status
#       print content

        #3rd
#        conn = httplib.HTTPConnection(url)
#        conn.request("GET")
#        response3 = conn.getresponse()
#        data = response.read()
#        conn.close

        watt = 0
        loopCount = 1

    else :
        loopCount+=1



