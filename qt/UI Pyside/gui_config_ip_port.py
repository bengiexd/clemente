# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_config_ip_port.ui'
#
# Created: Mon Nov 25 21:07:01 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 200)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 21, 16))
        self.label.setObjectName("label")
        self.text_edit_port = QtGui.QTextEdit(Dialog)
        self.text_edit_port.setGeometry(QtCore.QRect(110, 70, 201, 31))
        self.text_edit_port.setObjectName("text_edit_port")
        self.text_edit_ip = QtGui.QTextEdit(Dialog)
        self.text_edit_ip.setGeometry(QtCore.QRect(110, 30, 201, 31))
        self.text_edit_ip.setObjectName("text_edit_ip")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Ip:", None, QtGui.QApplication.UnicodeUTF8))

