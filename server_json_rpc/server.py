import cherrypy
import cpjsonrpcserver
import threading

class JsonRpcMethods(cpjsonrpcserver.JsonRpcMethods):

    def hello(self, name):
        return u"Hello " + name
    hello.exposed = True

    def multi(self, num):
        return num * 2
    multi.exposed = True
        
    def index(self, limit=4):
        return range(int(limit))
    index.exposed = True
        
    def status(self):
        return u"ok"
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
            cherrypy.tree.mount(JsonRpcMethods(), "/", None)
            cherrypy.engine.start()
        cherrypy.engine.block()

    def stop(self):
        with self.sync:
            cherrypy.engine.exit()
            cherrypy.server.stop()

def main():    
    server = HTTPServer()
    server.start()

if __name__ == "__main__":
    main()

