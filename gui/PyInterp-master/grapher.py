import os
os.environ['QT_API'] = 'pyside'

from PySide.QtGui   import *
from PySide.QtCore  import *

from PyInterp.QIPythonWidget import QIPythonWidget as QPython

import matplotlib

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.figure                  import Figure


class Graph(FigureCanvasQTAgg):

    def __init__(self, parent=None):
        super(Graph, self).__init__(Figure())


class Main(QWidget):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.graph   = Graph(self)
        self.ipython = QPython()

        self.ipython.setMinimumHeight(400)

        layout = QVBoxLayout(self)
        layout.addWidget(self.graph)
        layout.addWidget(self.ipython)


app = QApplication([])
main = Main()

namespace = main.ipython.get_user_namespace()
namespace['graph'] = main.graph
namespace['ipython'] = main.ipython

main.show()
app.exec_()
