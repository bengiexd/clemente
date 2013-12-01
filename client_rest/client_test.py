import urllib2
import json

url = "http://127.0.0.1:8080/?hello=bengie"
data = urllib2.urlopen(url).read()
data = json.loads(data)
print type(data)
print data
#print data["status"]


#{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}