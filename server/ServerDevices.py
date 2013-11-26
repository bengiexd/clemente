import time
import socket
import threading

from H_Device import Device

class Server(threading.Thread):
    
    """ 
        server
            _ip: localhost
            _port: 9000
            _nro_max_devices: 100
    """
    
    _ip = "127.0.0.1"
    _port = 9000
    _nro_max_devices = 100
    
    _activo = True

    def __init__(self, ip=_ip, port=_port):      
    	
    	"""	start the server """
        threading.Thread.__init__(self)
        
    	if ip:
            self._ip = ip
        if port:
            self._port = int(port)
            
    def run(self):
        try:
            self._socket_server = socket.socket()
            self._socket_server.bind((self._ip,self._port))
            self._socket_server.listen(self._nro_max_devices)
            print "server initiated"
            # accept devices
            self._accept_devices()
        except Exception, ex:
            print "error server don`t inizialized"
            self._activo = False
        
    def set_icaro(self,icaro):
        self.icaro = icaro

    def _accept_devices(self):
        
        """ accept the connection of any device """
        
        while self._activo:
            (sc, addr) = self._socket_server.accept()
            print "connected client: ",addr              
            device = Device()
            device.iniciar(sc)
            device.start()

    def shut_down_server(self):
    	
    	""" shut down the server """
    	
        self._socket_server.close()


