import sys
from PySide import QtCore, QtGui

sys.path.append('./../UI Pyside/')

from gui_remote_clemente import Ui_Dialog

class ConfigDialogRemoteClemente():

    def __init__(self, data_conex):
        
        self.Dialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        # atributes
        self.data_conex = data_conex

        self.buttons_leds = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0}
        self.add_icons_leds()
        
        # add functions
        self.add_functions()
        # add events
        self.add_events()
        # show
        self.show()
        
    def show(self):
        self.Dialog.show()          
        
    def add_icons_leds(self):
        self.icon_off = QtGui.QIcon()
        self.icon_off.addPixmap(QtGui.QPixmap("../media/images/led_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.icon_red = QtGui.QIcon()
        self.icon_red.addPixmap(QtGui.QPixmap("../media/images/led_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.icon_green = QtGui.QIcon()
        self.icon_green.addPixmap(QtGui.QPixmap("../media/images/led_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.ui.push_button_0.setIcon(self.icon_off)
        self.ui.push_button_1.setIcon(self.icon_off)
        self.ui.push_button_2.setIcon(self.icon_off)
        self.ui.push_button_3.setIcon(self.icon_off)
        self.ui.push_button_4.setIcon(self.icon_off)
        self.ui.push_button_5.setIcon(self.icon_off)
        self.ui.push_button_6.setIcon(self.icon_off)
        self.ui.push_button_7.setIcon(self.icon_off)
        
    def add_functions(self):
        self.ui.test = self.test
        
        self.ui.clicked_button_0 = self.clicked_button_0
        self.ui.clicked_button_1 = self.clicked_button_1
        self.ui.clicked_button_2 = self.clicked_button_2
        self.ui.clicked_button_3 = self.clicked_button_3
        self.ui.clicked_button_4 = self.clicked_button_4
        self.ui.clicked_button_5 = self.clicked_button_5
        self.ui.clicked_button_6 = self.clicked_button_6
        self.ui.clicked_button_7 = self.clicked_button_7
        
    def add_events(self):
        QtCore.QObject.connect(self.ui.push_button_test, QtCore.SIGNAL("clicked()"), self.ui.test)
                
        # events colors leds
        QtCore.QObject.connect(self.ui.push_button_0, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_0)
        QtCore.QObject.connect(self.ui.push_button_1, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_1)
        QtCore.QObject.connect(self.ui.push_button_2, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_2)
        QtCore.QObject.connect(self.ui.push_button_3, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_3)
        QtCore.QObject.connect(self.ui.push_button_4, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_4)
        QtCore.QObject.connect(self.ui.push_button_5, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_5)
        QtCore.QObject.connect(self.ui.push_button_6, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_6)
        QtCore.QObject.connect(self.ui.push_button_7, QtCore.SIGNAL("clicked()"), self.ui.clicked_button_7)
        
    def leds(self):
        n = ""
        for i in range(8):
            n += str(self.buttons_leds[str(i)])
        n = n[::-1]
        n = [int(n,2)]
        print n
        self.data_conex["http_client"].send(method='leds', data=n)
        
    # functions
    def test(self):
        command = [str(self.ui.text_edit_command.toPlainText())]
        if command is not "":            
            self.data_conex["http_client"].send(method='leds', data=command)
        else:
            print "error datos incorrectos"
            
    def clicked_button_0(self):
        if self.buttons_leds["0"] == 0:
            self.ui.push_button_0.setIcon(self.icon_red)
            self.buttons_leds["0"] = 1
        else:
            self.ui.push_button_0.setIcon(self.icon_off)
            self.buttons_leds["0"] = 0
        self.leds()  
            
    def clicked_button_1(self):
        if self.buttons_leds["1"] == 0:
            self.ui.push_button_1.setIcon(self.icon_green)
            self.buttons_leds["1"] = 1
        else:
            self.ui.push_button_1.setIcon(self.icon_off)
            self.buttons_leds["1"] = 0
        self.leds()
             
    def clicked_button_2(self):
        if self.buttons_leds["2"] == 0:
            self.ui.push_button_2.setIcon(self.icon_green)
            self.buttons_leds["2"] = 1
        else:
            self.ui.push_button_2.setIcon(self.icon_off)
            self.buttons_leds["2"] = 0
        self.leds()
    
    def clicked_button_3(self):
        if self.buttons_leds["3"] == 0:
            self.ui.push_button_3.setIcon(self.icon_green)
            self.buttons_leds["3"] = 1
        else:
            self.ui.push_button_3.setIcon(self.icon_off)
            self.buttons_leds["3"] = 0
        self.leds()
            
    def clicked_button_4(self):
        if self.buttons_leds["4"] == 0:
            self.ui.push_button_4.setIcon(self.icon_green)
            self.buttons_leds["4"] = 1
        else:
            self.ui.push_button_4.setIcon(self.icon_off)
            self.buttons_leds["4"] = 0
        self.leds()
            
    def clicked_button_5(self):
        if self.buttons_leds["5"] == 0:
            self.ui.push_button_5.setIcon(self.icon_green)
            self.buttons_leds["5"] = 1
        else:
            self.ui.push_button_5.setIcon(self.icon_off)
            self.buttons_leds["5"] = 0
        self.leds()
            
    def clicked_button_6(self):
        if self.buttons_leds["6"] == 0:
            self.ui.push_button_6.setIcon(self.icon_green)
            self.buttons_leds["6"] = 1
        else:
            self.ui.push_button_6.setIcon(self.icon_off)
            self.buttons_leds["6"] = 0
        self.leds()
    
    def clicked_button_7(self):
        if self.buttons_leds["7"] == 0:
            self.ui.push_button_7.setIcon(self.icon_green)
            self.buttons_leds["7"] = 1
        else:
            self.ui.push_button_7.setIcon(self.icon_off)
            self.buttons_leds["7"] = 0
        self.leds()
    
                   



