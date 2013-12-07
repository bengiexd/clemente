from PySide.QtGui  import *
from QIPythonWidget import QIPythonWidget

class Main(QWidget):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        layout = QVBoxLayout(self)

        self.button = QPushButton('Another widget')

        # Just like any other widget
        self.iPython = QIPythonWidget()

        layout.addWidget(self.button)
        layout.addWidget(self.iPython)


app  = QApplication([])


main = Main()

namespace = main.iPython.get_user_namespace()
namespace['main']    = main
namespace['foobar']  = 'value for foobar'
namespace['another'] = 'another test'

main.show()
app.exec_()
