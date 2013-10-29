

from PyQt4 import QtCore, QtGui

from main import Ui_MainWindow

class ConfigDialog():
    
    def __init__(self):
        #self.app = QtGui.QApplication(sys.argv)
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        
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
        self.ui.data_conex = {"ip":"", "port":""}           
        
    def add_functions(self):
        #self.ui.print_ok = self.print_ok
        self.ui.accept_data = self.accept_data
        
    def add_events(self):
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.action_search_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.config_search_clemente)
        QtCore.QObject.connect(self.action_search_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.print_data_conex)    
        
    # functions
    

class Ui_MainWindow(object):
    
    data_conex = {"ip":"", "port":""}    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuClemente = QtGui.QMenu(self.menubar)
        self.menuClemente.setObjectName(_fromUtf8("menuClemente"))
        self.menuClemente_2 = QtGui.QMenu(self.menubar)
        self.menuClemente_2.setObjectName(_fromUtf8("menuClemente_2"))
        self.menuIcaro = QtGui.QMenu(self.menubar)
        self.menuIcaro.setObjectName(_fromUtf8("menuIcaro"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.action_search_clemente = QtGui.QAction(MainWindow)
        self.action_search_clemente.setObjectName(_fromUtf8("action_search_clemente"))
        self.action_wait_clemente = QtGui.QAction(MainWindow)
        self.action_wait_clemente.setObjectName(_fromUtf8("action_wait_clemente"))
        self.action_search_icaro = QtGui.QAction(MainWindow)
        self.action_search_icaro.setObjectName(_fromUtf8("action_search_icaro"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.menuClemente.addAction(self.actionQuit)
        self.menuClemente_2.addAction(self.action_search_clemente)
        self.menuClemente_2.addAction(self.action_wait_clemente)
        self.menuIcaro.addAction(self.action_search_icaro)
        self.menuIcaro.addAction(self.actionConnect)
        self.menuIcaro.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuClemente.menuAction())
        self.menubar.addAction(self.menuClemente_2.menuAction())
        self.menubar.addAction(self.menuIcaro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.action_search_clemente, QtCore.SIGNAL(_fromUtf8("activated()")), self.config_search_clemente)
        QtCore.QObject.connect(self.action_search_icaro, QtCore.SIGNAL(_fromUtf8("activated()")), self.print_data_conex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuClemente.setTitle(_translate("MainWindow", "File", None))
        self.menuClemente_2.setTitle(_translate("MainWindow", "Clemente", None))
        self.menuIcaro.setTitle(_translate("MainWindow", "Icaro", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.action_search_clemente.setText(_translate("MainWindow", "Search", None))
        self.action_wait_clemente.setText(_translate("MainWindow", "Wait", None))
        self.action_search_icaro.setText(_translate("MainWindow", "Search", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect", None))

    def config_search_clemente(self):
        #a = ClementeSearch(self.ip,self.port)
        a = ConfigDialog()
        a.data(self.data_conex)
        a.run()
        
    def print_data_conex(self):
        print self.data_conex

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

