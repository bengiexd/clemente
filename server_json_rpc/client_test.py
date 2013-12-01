import urllib2
import json

url = 'http://127.0.0.1:8080/'
data = json.dumps({"jsonrpc": "2.0", "method": "hello", "params": ['bengie'], "id": 1})
headers = {'Content-Type': 'application/json'}

req = urllib2.Request(url, data, headers=headers)
f = urllib2.urlopen(req)
response = f.read()
f.close()

data = json.loads(response)
print type(data)
print data