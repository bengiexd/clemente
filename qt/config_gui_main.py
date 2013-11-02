import sys
from PyQt4 import QtCore, QtGui

from gui_main import Ui_MainWindow
from config_search_clemente import ConfigDialogSearchClemente
from config_wait_clemente import ConfigDialogWaitClemente

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
        self.data_conex = {"ip":"", "port":"", "socket":None}
        
        # add events
        self.add_events()

        self.run()

    def run(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def add_events(self):
        #QtCore.QObject.connect(self.ui.action_search_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.see_data)
        QtCore.QObject.connect(self.ui.action_search_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.search_clemente)
        QtCore.QObject.connect(self.ui.action_wait_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.wait_clemente)
        #QtCore.QObject.connect(self.action_search_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.print_data_conex)
        
    # functions
    def see_data(self):
        ip = self.data_conex["ip"]
        port = self.data_conex["port"]
        print ip, port
        
    def search_clemente(self):        
        form = ConfigDialogSearchClemente(self.data_conex)
        
    def wait_clemente(self):
        form = ConfigDialogWaitClemente(self.data_conex)

c = ConfigMain()
    
    
