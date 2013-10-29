# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_search.ui'
#
# Created: Tue Oct 22 07:52:57 2013
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_form_config_search(object):
    def setupUi(self, form_config_search):
        form_config_search.setObjectName(_fromUtf8("form_config_search"))
        form_config_search.resize(334, 188)
        self.textEdit = QtGui.QTextEdit(form_config_search)
        self.textEdit.setGeometry(QtCore.QRect(80, 20, 201, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(form_config_search)
        self.label.setGeometry(QtCore.QRect(50, 30, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(form_config_search)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 59, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_2 = QtGui.QTextEdit(form_config_search)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 60, 201, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.push_button_ok = QtGui.QPushButton(form_config_search)
        self.push_button_ok.setGeometry(QtCore.QRect(110, 120, 94, 27))
        self.push_button_ok.setObjectName(_fromUtf8("push_button_ok"))

        self.retranslateUi(form_config_search)
        QtCore.QObject.connect(self.push_button_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), form_config_search.close)
        QtCore.QMetaObject.connectSlotsByName(form_config_search)

    def retranslateUi(self, form_config_search):
        form_config_search.setWindowTitle(_translate("form_config_search", "Form", None))
        self.label.setText(_translate("form_config_search", "Ip:", None))
        self.label_2.setText(_translate("form_config_search", "Puerto:", None))
        self.push_button_ok.setText(_translate("form_config_search", "OK", None))


class GUISearch():
    def __init__(self):
        import sys
        app = QtGui.QApplication(sys.argv)
        form_config_search = QtGui.QWidget()
        ui = Ui_form_config_search()
        ui.setupUi(form_config_search)
        form_config_search.show()
        sys.exit(app.exec_())

class Interface():
    def main(self):
        a = GUISearch()
        

        
  
        
        
        
        
        
        
