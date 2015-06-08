#!/usr/bin/env python

import httplib, urllib, urllib2
import serial
import time
import re
import numpy

ser = serial.Serial('/dev/ttyACM0', 9600)
pattern = re.compile("^\s+|\s*,\s*|\s+$")

resetCount = 15*1
wattHourList = []

while 1 :
    serialValue = ser.readline() 
    print serialValue    
    splitValues = pattern.split(serialValue) 

    if(len(wattHourList) == resetCount-1) :
        wattHourList.append(splitValues[0])
        url = '202.30.29.239:8888/update.php'
        values = {'watt' : numpy.mean(wattHourList),
            'power' : serialValues[1]}

        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        
        print response.status, response.reason

        conn.close()


    else :
        wattHourList.append(splitValues[0])




