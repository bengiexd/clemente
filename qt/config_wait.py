# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_wait.ui'
#
# Created: Tue Oct 22 07:53:17 2013
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

class Ui_form_config_wait(object):
    def setupUi(self, form_config_wait):
        form_config_wait.setObjectName(_fromUtf8("form_config_wait"))
        form_config_wait.resize(343, 241)
        self.label_2 = QtGui.QLabel(form_config_wait)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 59, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(form_config_wait)
        self.label.setGeometry(QtCore.QRect(60, 40, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(form_config_wait)
        self.textEdit.setGeometry(QtCore.QRect(90, 30, 201, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(form_config_wait)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 70, 201, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.push_button_ok = QtGui.QPushButton(form_config_wait)
        self.push_button_ok.setGeometry(QtCore.QRect(120, 130, 94, 27))
        self.push_button_ok.setObjectName(_fromUtf8("push_button_ok"))

        self.retranslateUi(form_config_wait)
        QtCore.QObject.connect(self.push_button_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), form_config_wait.close)
        QtCore.QMetaObject.connectSlotsByName(form_config_wait)

    def retranslateUi(self, form_config_wait):
        form_config_wait.setWindowTitle(_translate("form_config_wait", "Form", None))
        self.label_2.setText(_translate("form_config_wait", "Puerto:", None))
        self.label.setText(_translate("form_config_wait", "Ip:", None))
        self.push_button_ok.setText(_translate("form_config_wait", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form_config_wait = QtGui.QWidget()
    ui = Ui_form_config_wait()
    ui.setupUi(form_config_wait)
    form_config_wait.show()
    sys.exit(app.exec_())

