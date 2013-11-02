# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_test_clemente.ui'
#
# Created: Sat Nov  2 11:44:43 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(455, 231)
        self.push_button_test = QtGui.QPushButton(Dialog)
        self.push_button_test.setGeometry(QtCore.QRect(260, 140, 94, 27))
        self.push_button_test.setObjectName(_fromUtf8("push_button_test"))
        self.text_edit_command = QtGui.QTextEdit(Dialog)
        self.text_edit_command.setGeometry(QtCore.QRect(190, 80, 181, 31))
        self.text_edit_command.setObjectName(_fromUtf8("text_edit_command"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.push_button_exit = QtGui.QPushButton(Dialog)
        self.push_button_exit.setGeometry(QtCore.QRect(140, 140, 94, 27))
        self.push_button_exit.setObjectName(_fromUtf8("push_button_exit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.push_button_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Test Clemente", None))
        self.push_button_test.setText(_translate("Dialog", "Test", None))
        self.label.setText(_translate("Dialog", "Command", None))
        self.push_button_exit.setText(_translate("Dialog", "Exit", None))

