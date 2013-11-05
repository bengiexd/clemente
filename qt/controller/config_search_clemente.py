import sys
from PyQt4 import QtCore, QtGui
from gui_config_ip_port import Ui_Dialog

sys.path.append('./../UI/')

sys.path.append('../../client/')
from cliente import Cliente

class ConfigDialogSearchClemente():
    
    def __init__(self, data_conex):

        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        # atributes
        self.data_conex = data_conex
        # add functions
        self.add_functions()        
        # add events
        self.add_events()        
        # show
        self.show()
        
        
    def show(self):        
        self.Dialog.show()

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
            self.data_conex["ip"] = _ip
            self.data_conex["port"] = _port
            
            # search one specified server with client            
            self.data_conex["socket"] = Cliente(_ip, _port)
            
            if self.data_conex["socket"].connect_with_server():
                print "conectado al server"
            else:
                print "not accept"
            
            self.Dialog.accept()
        else:
            print "error datos incorrectos"


