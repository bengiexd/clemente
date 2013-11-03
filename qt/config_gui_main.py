import sys
from PyQt4 import QtCore, QtGui

from gui_main import Ui_MainWindow
from config_search_clemente import ConfigDialogSearchClemente
from config_wait_clemente import ConfigDialogWaitClemente
from config_gui_test_icaro import ConfigDialogTestIcaro
from config_gui_test_clemente import ConfigDialogTestClemente

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

"""
    data_conex = {"ip":"", "port":"", "socket":None}
"""

class ConfigMain():
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # atributes
        self.icaro = None
        self.data_conex = {"ip":"", "port":"", "socket":None}
        
        # add functions 
        self.add_functions()
        
        # add events
        self.add_events()

        self.run()

    def run(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def add_functions(self):
        self.ui.search_clemente = self.search_clemente
        self.ui.wait_clemente = self.wait_clemente
        self.ui.test_clemente = self.test_clemente
        self.ui.connect_icaro = self.connect_icaro
        self.ui.test_icaro = self.test_icaro
        self.ui.disconnect_icaro = self.disconnect_icaro        

    def add_events(self):
        QtCore.QObject.connect(self.ui.action_search_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.ui.search_clemente)
        QtCore.QObject.connect(self.ui.action_wait_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.ui.wait_clemente)
        QtCore.QObject.connect(self.ui.action_connect_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.ui.connect_icaro)
        QtCore.QObject.connect(self.ui.action_disconnect_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.ui.disconnect_icaro)
        QtCore.QObject.connect(self.ui.action_test_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.ui.test_icaro)
        QtCore.QObject.connect(self.ui.action_test_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.ui.test_clemente)
        
        
    # functions
    def see_data(self):
        ip = self.data_conex["ip"]
        port = self.data_conex["port"]
        print ip, port
        
    def search_clemente(self):
        form = ConfigDialogSearchClemente(self.data_conex)
        
    def wait_clemente(self):
        form = ConfigDialogWaitClemente(self.data_conex, self.icaro)
        
    def test_clemente(self):
        form = ConfigDialogTestClemente(self.data_conex["socket"])
        
    def connect_icaro(self):
        import apicaro
        port = apicaro.puerto()
        if port.iniciar():
            self.icaro = port
            print "icaro connect succesfull"
        else:
            print "error: icaro don't connect"
            
    def test_icaro(self):
        if self.icaro is not None:
            form = ConfigDialogTestIcaro(self.icaro)
        else:
            print "error icaro don`t exists"
            
    def disconnect_icaro(self):
        if self.icaro is not None:
            if self.icaro.cerrar():
                print "close correct"
        else:
            print "error when close icaro"

c = ConfigMain()
    
    
