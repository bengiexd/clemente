import urllib2
import json

class HttpClient():
    
    _ip = '127.0.0.1'
    _port = 8080
    
    HEADERS = {'Content-Type': 'application/json'}
    
    def __init__(self, ip=_ip, port=_port):
        if ip:
            self._ip = ip
        if port:
            self._port = port

        self.url_server = "http://%s:%i/" % (self._ip, self._port)
        #print self.url_server
    
    def send(self, method='status', data=None):
        if data:
            data_json = json.dumps({"jsonrpc": "2.0", "method": method, "params": data, "id": 1})
        else:
            data_json = json.dumps({"jsonrpc": "2.0", "method": method, "id": 1})
        try:
            req = urllib2.Request(self.url_server, data_json, headers=self.HEADERS)
            connect = urllib2.urlopen(req)
            response = connect.read()
            connect.close()
            data_json = json.loads(response)
            return data_json['result']
        except Exception, ex:
            return None

    def server_available(self):        
        resp = self.send(method='status')
        if resp is None:
            return False
        if resp == 'ok':
            return True
        return False

"""
# TEST
client = HttpClient()
client.server_available()
#print client.send('hello', ['bengie'])
"""
