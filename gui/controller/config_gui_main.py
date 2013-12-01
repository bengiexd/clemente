import sys
import time

from PySide import QtCore, QtGui

sys.path.append('./../UI Pyside/')

from gui_main import Ui_MainWindow

from config_search_clemente import ConfigDialogSearchClemente
from config_wait_clemente import ConfigDialogWaitClemente
from config_gui_test_icaro import ConfigDialogTestIcaro
from config_gui_test_clemente import ConfigDialogTestClemente

"""
    data_conex = {"ip":"", "port":"", "socket":None}
"""

class ConfigMain():
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.MainWindow.adjustSize()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        #details
        # -- icon application
        self.MainWindow.setWindowIcon(QtGui.QIcon('./../media/icon/icaro.png'))
        self.MainWindow.showMaximized()
        # create actions
        self.create_actions()
        # create toolbar
        self.create_tool_bars()
        # atributes
        self.icaro = None
        self.ui.data_conex = {"ip":"", "port":"", "status_clemente":QtGui.QTextEdit(), "socket":None}
        self.ui.data_conex["status_clemente"].setText("stop")
        # add functions
        self.add_functions()
        # add events
        self.add_events()
        self.show()

    def show(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())
        
    def create_actions(self):
        # for clemente
        self.ui.act_search_clemente = QtGui.QAction(QtGui.QIcon('./../media/icon/clemente-search.png'), "Search Clemente", self.MainWindow)        
        self.ui.act_search_clemente.triggered.connect(self.search_clemente)
        self.ui.act_wait_clemente = QtGui.QAction(QtGui.QIcon('./../media/icon/wait_clemente.png'), "Wait Clemente", self.MainWindow)
        self.ui.act_wait_clemente.triggered.connect(self.wait_clemente)
        self.ui.act_test_clemente = QtGui.QAction(QtGui.QIcon('./../media/icon/clemente-test.png'), "Test Clemente", self.MainWindow)
        self.ui.act_test_clemente.triggered.connect(self.test_clemente)
        self.ui.act_exit = QtGui.QAction(QtGui.QIcon('./../media/icon/exit.png'), "Exit", self.MainWindow)
        self.ui.act_exit.triggered.connect(self.MainWindow.close)
        # for icaro
        self.ui.act_icaro_connect = QtGui.QAction(QtGui.QIcon('./../media/icon/icaro.png'), "Connect Icaro", self.MainWindow)        
        self.ui.act_icaro_connect.triggered.connect(self.connect_icaro)
        self.ui.act_icaro_disconnect = QtGui.QAction(QtGui.QIcon('./../media/icon/icaro.png'), "Disconnect Icaro", self.MainWindow)        
        self.ui.act_icaro_disconnect.triggered.connect(self.disconnect_icaro)
        self.ui.act_icaro_test = QtGui.QAction(QtGui.QIcon('./../media/icon/icaro.png'), "Test Icaro", self.MainWindow)        
        self.ui.act_icaro_test.triggered.connect(self.test_icaro)

    def create_tool_bars(self):
        # options clemente
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Search Clemente"))
        fileToolBar.addAction(self.ui.act_search_clemente)
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Wait Clemente"))
        fileToolBar.addAction(self.ui.act_wait_clemente)
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Test Clemente"))
        fileToolBar.addAction(self.ui.act_test_clemente)        
        # options icaro
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Connect Icaro"))
        fileToolBar.addAction(self.ui.act_icaro_connect)
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Disconnect Icaro"))
        fileToolBar.addAction(self.ui.act_icaro_disconnect)
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Test Icaro"))
        fileToolBar.addAction(self.ui.act_icaro_test)
        # options extra
        fileToolBar = self.MainWindow.addToolBar(self.MainWindow.tr("Exit"))
        fileToolBar.addAction(self.ui.act_exit)

    def add_functions(self):
        self.ui.search_clemente = self.search_clemente
        self.ui.wait_clemente = self.wait_clemente
        self.ui.test_clemente = self.test_clemente
        self.ui.connect_icaro = self.connect_icaro
        self.ui.test_icaro = self.test_icaro
        self.ui.disconnect_icaro = self.disconnect_icaro     
        self.ui.change_state_clemente = self.change_state_clemente   

    def add_events(self):
        QtCore.QObject.connect(self.ui.action_search_clemente, QtCore.SIGNAL("activated()"), self.ui.search_clemente)
        QtCore.QObject.connect(self.ui.action_wait_clemente, QtCore.SIGNAL("activated()"), self.ui.wait_clemente)
        QtCore.QObject.connect(self.ui.action_connect_icaro, QtCore.SIGNAL("activated()"), self.ui.connect_icaro)
        QtCore.QObject.connect(self.ui.action_disconnect_icaro, QtCore.SIGNAL("activated()"), self.ui.disconnect_icaro)
        QtCore.QObject.connect(self.ui.action_test_icaro, QtCore.SIGNAL("activated()"), self.ui.test_icaro)
        QtCore.QObject.connect(self.ui.action_test_clemente, QtCore.SIGNAL("activated()"), self.ui.test_clemente)
        QtCore.QObject.connect(self.ui.data_conex["status_clemente"], QtCore.SIGNAL("textChanged()"), self.ui.change_state_clemente)        
        
    # functions
    def see_data(self):
        ip = self.ui.data_conex["ip"]
        port = self.ui.data_conex["port"]
        print ip, port

    def search_clemente(self):
        form = ConfigDialogSearchClemente(self.ui.data_conex)

    def wait_clemente(self):
        state = self.ui.data_conex["status_clemente"].toPlainText()
        if state == "wait":
            # stop server
            self.ui.data_conex["http_server"].stop()
            self.ui.data_conex["status_clemente"].setText("stop")
            self.ui.action_wait_clemente.setText("Wait")
            self.ui.act_wait_clemente.setText("Wait")
            self.ui.act_wait_clemente.setIcon(QtGui.QIcon('./../media/icon/wait_clemente.png'))
        elif state == "stop":
            form = ConfigDialogWaitClemente(self.ui.data_conex, self.icaro) 

    def test_clemente(self):
        form = ConfigDialogTestClemente(self.ui.data_conex["socket"])
        
    def change_state_clemente(self):
        state = self.ui.data_conex["status_clemente"].toPlainText()
        if state == "wait":
            # set text action
            self.ui.act_wait_clemente.setText("Stop Wait")
            self.ui.action_wait_clemente.setText("Stop Wait")
            self.ui.act_wait_clemente.setIcon(QtGui.QIcon('./../media/icon/clemente_stop.png'))
        elif state == "stop":
            pass
        
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

