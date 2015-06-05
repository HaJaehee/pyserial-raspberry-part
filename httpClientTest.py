#!/usr/bin/env python

import httplib, urllib
params = urllib.urlencode({'device-reg-id':1234})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("127.0.0.1:8888")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
data
conn.close()
