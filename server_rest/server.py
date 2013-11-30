from __future__ import with_statement
import cherrypy
import threading
from simplejson import JSONEncoder

encoder = JSONEncoder()

import json

def jsonify_tool_callback(*args, **kwargs):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    response.body = encoder.iterencode(response.body)

cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', jsonify_tool_callback, priority=30)


class Server(object):

    @cherrypy.tools.jsonify()
    def index(self, limit=4):
        return range(int(limit))
    index.exposed = True
    
    #@cherrypy.tools.jsonify()
    def status(self):
        return json.dumps({'status':'ok'})
    status.exposed = True

class HTTPServer(threading.Thread):
    
    _ip = "127.0.0.1"
    _port = 8080
    
    def __init__(self, ip=_ip, port=_port):
        if ip:
            self._ip = ip
        if port:
            self._port = port
        
        threading.Thread.__init__(self)
        self.sync = threading.Condition()

    def run(self):
        with self.sync:
            cherrypy.server.socket_port = self._port
            #cherrypy.server.socket_host = optional hostname
            cherrypy.tree.mount(Server(), "/", None)
            cherrypy.engine.start()
        cherrypy.engine.block()

    def stop(self):
        with self.sync:
            cherrypy.engine.exit()
            cherrypy.server.stop()
   
# TEST
"""
server = HTTPServer()
server.start()
"""
