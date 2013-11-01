import sys
from PyQt4 import QtCore, QtGui

from main import Ui_MainWindow
from config_search import ConfigDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ConfigMain():
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # add atributes
        self.add_atributes()
        # add functions
        #self.add_functions()
        # add events
        self.add_events()

        self.run()

    def run(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def add_atributes(self):
        self.ui.data_conex = {"ip":"", "port":""}        

    def add_functions(self):     
        self.ui.see_data = self.see_data

    def add_events(self):        
        #QtCore.QObject.connect(self.ui.action_search_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.see_data)
        QtCore.QObject.connect(self.ui.action_search_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.search_clemente)
        #QtCore.QObject.connect(self.action_search_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.print_data_conex)
        
    # functions
    def see_data(self):
        ip = self.ui.data_conex["ip"]
        port = self.ui.data_conex["ip"]
        print ip, port
        
    def search_clemente(self):
        c = ConfigDialog(self.ui.data_conex)
        c.run()

c = ConfigMain()
    
    
