import sys
from PySide import QtCore, QtGui

sys.path.append('./../UI Pyside/')
sys.path.append('../../server_json_rpc/')

from gui_config_ip_port import Ui_Dialog
from server import HTTPServer

class ConfigDialogWaitClemente():

    def __init__(self, data_conex, icaro):
        
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        
        # set window title
        self.Dialog.setWindowTitle('Wait Clemente')
        # atributes
        self.ui.data_conex = data_conex
        self.icaro = icaro
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
            self.ui.data_conex["ip"] = _ip
            self.ui.data_conex["port"] = int(_port)
            # search one specified server with client
            self.ui.data_conex["http_server"] = HTTPServer(ip=_ip, port=self.ui.data_conex["port"])            
            # start thread of server
            self.ui.data_conex["http_server"].start()
            self.ui.data_conex["status_clemente"].setText("wait")            
            self.Dialog.accept()
        else:
            print "error datos incorrectos"



