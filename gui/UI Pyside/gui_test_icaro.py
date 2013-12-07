# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_test_icaro.ui'
#
# Created: Mon Nov 25 21:08:15 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 231)
        self.push_button_test = QtGui.QPushButton(Dialog)
        self.push_button_test.setGeometry(QtCore.QRect(260, 140, 94, 27))
        self.push_button_test.setObjectName("push_button_test")
        self.text_edit_command = QtGui.QTextEdit(Dialog)
        self.text_edit_command.setGeometry(QtCore.QRect(190, 80, 181, 31))
        self.text_edit_command.setObjectName("text_edit_command")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 71, 16))
        self.label.setObjectName("label")
        self.push_button_exit = QtGui.QPushButton(Dialog)
        self.push_button_exit.setGeometry(QtCore.QRect(140, 140, 94, 27))
        self.push_button_exit.setObjectName("push_button_exit")

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.push_button_test, QtCore.SIGNAL("clicked()"), self.text_edit_command.clear)
        QtCore.QObject.connect(self.push_button_exit, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Test Icaro", None, QtGui.QApplication.UnicodeUTF8))
        self.push_button_test.setText(QtGui.QApplication.translate("Dialog", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.push_button_exit.setText(QtGui.QApplication.translate("Dialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))

