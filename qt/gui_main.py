# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main.ui'
#
# Created: Sat Nov  2 10:37:51 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
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
        self.action_connect_icaro = QtGui.QAction(MainWindow)
        self.action_connect_icaro.setObjectName(_fromUtf8("action_connect_icaro"))
        self.action_disconnect_icaro = QtGui.QAction(MainWindow)
        self.action_disconnect_icaro.setObjectName(_fromUtf8("action_disconnect_icaro"))
        self.action_test_icaro = QtGui.QAction(MainWindow)
        self.action_test_icaro.setObjectName(_fromUtf8("action_test_icaro"))
        self.action_test_clemente = QtGui.QAction(MainWindow)
        self.action_test_clemente.setObjectName(_fromUtf8("action_test_clemente"))
        self.menuClemente.addAction(self.actionQuit)
        self.menuClemente_2.addAction(self.action_search_clemente)
        self.menuClemente_2.addAction(self.action_wait_clemente)
        self.menuClemente_2.addAction(self.action_test_clemente)
        self.menuIcaro.addAction(self.action_search_icaro)
        self.menuIcaro.addAction(self.action_connect_icaro)
        self.menuIcaro.addAction(self.action_disconnect_icaro)
        self.menuIcaro.addAction(self.action_test_icaro)
        self.menubar.addAction(self.menuClemente.menuAction())
        self.menubar.addAction(self.menuClemente_2.menuAction())
        self.menubar.addAction(self.menuIcaro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
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
        self.action_connect_icaro.setText(_translate("MainWindow", "Connect", None))
        self.action_disconnect_icaro.setText(_translate("MainWindow", "Disconnect", None))
        self.action_test_icaro.setText(_translate("MainWindow", "Test", None))
        self.action_test_clemente.setText(_translate("MainWindow", "Test", None))

