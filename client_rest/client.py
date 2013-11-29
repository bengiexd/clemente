import urllib2
import json

url = "http://127.0.0.1:8080/?limit=32"
data = urllib2.urlopen(url).read()
data = json.loads(data)
print data

