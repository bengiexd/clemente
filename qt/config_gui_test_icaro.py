import sys
from PyQt4 import QtCore, QtGui
from gui_test_icaro import Ui_Dialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ConfigDialogTestIcaro():
    
    def __init__(self, icaro):
        
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        # atributes
        self.icaro = icaro
        # add functions
        self.add_functions()
        # add events
        self.add_events()
        # show
        self.show()
        
    def show(self):
        self.Dialog.show()  
        
    def add_functions(self):
        self.ui.test = self.test
        
    def add_events(self):        
        QtCore.QObject.connect(self.ui.push_button_test, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ui.test)
        
    # functions
    def test(self):
        _command = str(self.ui.text_edit_command.toPlainText())        
        if _command is not "":
            self.icaro.activar(int(_command))
        else:
            print "error datos incorrectos"



