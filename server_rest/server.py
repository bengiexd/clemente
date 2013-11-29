import cherrypy
from simplejson import JSONEncoder

encoder = JSONEncoder()

def jsonify_tool_callback(*args, **kwargs):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    response.body = encoder.iterencode(response.body)

cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', jsonify_tool_callback, priority=30)

class Root(object):
    @cherrypy.tools.jsonify()
    def index(self, limit=4):
        return range(int(limit))
    index.exposed = True

cherrypy.quickstart(Root())

