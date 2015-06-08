#!/usr/bin/env python

import httplib, urllib
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
    
    if(len(wattHourList) == resetCount) : 
        params = urllib.urlencode({'watt':numpy.mean(wattHourList),'power':splitValues[1]})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        
        #conn = httplib.HTTPConnection("202.30.29.239:8888")
        conn = httplib.HTTPConnection("127.0.0.1:8888")
        conn.request("POST", "", params, headers)
        
        response = conn.getresponse()
        print response.status, response.reason
        
        data = response.read()
        data
        
        conn.close()
        
        
    else :
        wattHourList.append(splitValues[0])
      
        
        
        
