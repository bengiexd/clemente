from PySide.QtGui import *
from PySide.QtCore import *
 
class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        QMenuBar.__init__(self, parent)
 
        newFileQAction = QAction(u'New...', self)
        newFileQAction.triggered.connect(self.newFileAction)
        newFileMenu = self.addMenu('&File')
        newFileMenu.addAction(newFileQAction)
 
        #self.addMenu('&Data')
        #self.addMenu('&Edit')
        #self.addMenu('&Windows')
        #self.addMenu('&About')

    def newFileAction(self):
        print("A")

