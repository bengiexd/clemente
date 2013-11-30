import urllib2
import json

class HttpClient():
    
    _ip = '127.0.0.1'
    _port = 8080
    
    def __init__(self, ip=_ip, port=_port):
        if ip:
            self._ip = ip
        if port:
            self._port = port

        self.url_server = "http://%s:%i/" % (self._ip, self._port)
        #print self.url_server
    
    def send(self, data):
        query = self.url_server + "?limit=12"
        data = urllib2.urlopen(url).read()
        data = json.loads(data)
        print data

    def connect_with_server(self):
        try:
            query = self.url_server + "status"            
            data = urllib2.urlopen(query).read()
            data = json.loads(data)                        
            if data['status'] == 'ok':
                return True
        except Exception, ex:
            print "Server Unavailable"
        return False

# TEST
"""
client = HttpClient()
client.connect_with_server()
"""