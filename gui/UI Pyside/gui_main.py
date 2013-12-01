# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main.ui'
#
# Created: Sun Dec  1 01:29:47 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuClemente = QtGui.QMenu(self.menubar)
        self.menuClemente.setObjectName("menuClemente")
        self.menuClemente_2 = QtGui.QMenu(self.menubar)
        self.menuClemente_2.setObjectName("menuClemente_2")
        self.menuIcaro = QtGui.QMenu(self.menubar)
        self.menuIcaro.setObjectName("menuIcaro")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.action_search_clemente = QtGui.QAction(MainWindow)
        self.action_search_clemente.setObjectName("action_search_clemente")
        self.action_wait_clemente = QtGui.QAction(MainWindow)
        self.action_wait_clemente.setObjectName("action_wait_clemente")
        self.action_search_icaro = QtGui.QAction(MainWindow)
        self.action_search_icaro.setObjectName("action_search_icaro")
        self.action_connect_icaro = QtGui.QAction(MainWindow)
        self.action_connect_icaro.setObjectName("action_connect_icaro")
        self.action_disconnect_icaro = QtGui.QAction(MainWindow)
        self.action_disconnect_icaro.setObjectName("action_disconnect_icaro")
        self.action_test_icaro = QtGui.QAction(MainWindow)
        self.action_test_icaro.setObjectName("action_test_icaro")
        self.action_remote_clemente = QtGui.QAction(MainWindow)
        self.action_remote_clemente.setObjectName("action_remote_clemente")
        self.menuClemente.addAction(self.actionQuit)
        self.menuClemente_2.addAction(self.action_search_clemente)
        self.menuClemente_2.addAction(self.action_wait_clemente)
        self.menuClemente_2.addAction(self.action_remote_clemente)
        self.menuIcaro.addAction(self.action_search_icaro)
        self.menuIcaro.addAction(self.action_connect_icaro)
        self.menuIcaro.addAction(self.action_disconnect_icaro)
        self.menuIcaro.addAction(self.action_test_icaro)
        self.menubar.addAction(self.menuClemente.menuAction())
        self.menubar.addAction(self.menuClemente_2.menuAction())
        self.menubar.addAction(self.menuIcaro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Clemente 0.3", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClemente.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClemente_2.setTitle(QtGui.QApplication.translate("MainWindow", "Clemente", None, QtGui.QApplication.UnicodeUTF8))
        self.menuIcaro.setTitle(QtGui.QApplication.translate("MainWindow", "Icaro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_search_clemente.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.action_wait_clemente.setText(QtGui.QApplication.translate("MainWindow", "Wait", None, QtGui.QApplication.UnicodeUTF8))
        self.action_search_icaro.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.action_connect_icaro.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.action_disconnect_icaro.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.action_test_icaro.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remote_clemente.setText(QtGui.QApplication.translate("MainWindow", "Control Remote", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remote_clemente.setToolTip(QtGui.QApplication.translate("MainWindow", "Remote", None, QtGui.QApplication.UnicodeUTF8))

