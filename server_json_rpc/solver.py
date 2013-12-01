class SolveRequest():
    
    icaro = None
    direcciones = {'ADELANTE':"Adelante",'ATRAS':"Atras",
                   'IZQUIERDA':'Izquierda','DERECHA':"Derecha",
                   'LEDS':'Leds'}

    def send_data_icaro(self, method, data):
        if self.icaro is None:
            return None
        if method is "activar":
            self.icaro.activar(data)
        elif method is "activar_servo":
            self.icaro.activar_servo(data[0],data[1])

    def solve(self, method, data):
        """
            Funcion que resuelve una peticion
        """
        if self.direcciones.has_key(method):
            if method is 'LEDS':
                self.leds(data)
                return True 
        return False            
    
    def leds(self, num):
        print 'leds ', num
        self.send_data_icaro('activar', num)

    def Adelante(self):
        self.send_data_icaro('activar_servo', 1,200)

    def Atras(self):
        self.send_data_icaro('activar_servo', 1,200)




