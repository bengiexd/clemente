QIPythonWidget
==============

Embedded python interpreter for PyQt4/PySide using the IPython project.
Tested with python 2.7 and IPython 0.13.1

This was build from a stackoverflow <a href="http://stackoverflow.com/questions/11513132/embedding-ipython-qt-console-in-a-pyqt-application">question</a>

## Example

```python
from QIPythonWidget import QIPythonWidget
from PySide.QtGui  import *

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

# assigen vars to user namespace
namespace = main.iPython.get_user_namespace()
namespace['main']    = main
namespace['foobar']  = 'value for foobar'
namespace['another'] = 'another test'

main.show()
app.exec_()
```

## Using pyqt instead of pyside
To use PyQt4 instead of pyside, it's necessary to set the QT_API environment variable to "pyqt".
It's also necessary for your code to use <a href="http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html">pyqt API v2</a> (not default in Python 2.x), which replaces some data types such as QString with built-in Python data types. 
