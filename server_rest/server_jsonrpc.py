import cherrypy
import cpjsonrpc

class JsonRpcMethods(cpjsonrpc.JsonRpcMethods):

    def hello(self, name):
        return u"Hello " + name
    hello.exposed = True


    def multi(self, num):
        return num * 2
    multi.exposed = True

def main():
    cherrypy.quickstart(JsonRpcMethods(debug = True))

if __name__ == "__main__":
    main()