import sys
from PyQt4 import QtCore, QtGui
from dialog_config_wait import Ui_Dialog

sys.path.append('./../client/')
from cliente import Cliente

class ConfigDialog():
    
    def __init__(self, data_conex):
        
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        
        self.ui.data_conex = data_conex
        # add atributes
        self.add_atributes()
        # add functions
        self.add_functions()
        # add events
        self.add_events()
        
    def data(self,data):
        """ function to receive vars of this father """
        self.data_conex = data
        
    def run(self):
        self.Dialog.show()
        #sys.exit(self.app.exec_())
                
    def add_atributes(self):
        pass
        
    def add_functions(self):        
        self.ui.accept_data = self.accept_data
        
    def add_events(self):
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.ui.accept_data)    
        
    # functions
    def print_ok(self):
        print self.ui.text_edit_ip.toPlainText()
        
    def accept_data(self):        
        _ip = str(self.ui.text_edit_ip.toPlainText())
        _port = str(self.ui.text_edit_port.toPlainText())
        if _ip is not "" and _port is not "":
            self.ui.data_conex["ip"] = _ip
            self.ui.data_conex["port"] = _port
            
            # search one specified server with client
            cliente = Cliente(_ip, _port)
            
            if cliente.connect_with_server():
                print "accept"
            else:
                print "not accept"
            
            self.Dialog.accept()
        else:
            print "error datos incorrectos"



