import cherrypy
import cpjsonrpcserver
import threading

from solver import SolveRequest

#_solver = None

class JsonRpcMethods(cpjsonrpcserver.JsonRpcMethods):    

    def hello(self, name):
        return u"Hello " + name
    hello.exposed = True

    def leds(self, num):        
        _solver.solve('LEDS', num)
        return u"ok"
    leds.exposed = True

    def index(self, limit=4):
        return range(int(limit))
    index.exposed = True

    def status(self):
        return u"ok"
    status.exposed = True

class HTTPServer(threading.Thread):
    
    def __init__(self, data_conex):
        self.data_conex = data_conex
        icaro = self.data_conex["icaro"]
        global _solver
        _solver = SolveRequest()
        _solver.set_icaro(icaro)

        threading.Thread.__init__(self)
        self.sync = threading.Condition()

    def run(self):        
        
        with self.sync:
            cherrypy.server.socket_port = self.data_conex["port"]
            #cherrypy.server.socket_host = optional hostname
            cherrypy.tree.mount(JsonRpcMethods(), "/", None)
            cherrypy.engine.start()
        cherrypy.engine.block()

    def stop(self):
        with self.sync:
            cherrypy.engine.exit()
            cherrypy.server.stop()

# TEST
"""
def main():    
    server = HTTPServer()
    server.start()

if __name__ == "__main__":
    main()
"""

