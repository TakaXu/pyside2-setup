# coding: utf-8
from PySide2.QtCore import *
from PySide2.QtWidgets  import *

import sys

class A(QMainWindow):
    def __init__(self, parent=None):
        super(A, self).__init__(parent)
        a = QFileSystemModel(self)
        a.setRootPath(QDir.homePath())

        v = QTreeView(self)
        v.setModel(a)
        self.setCentralWidget(v)

app = QApplication([])
m = A()
m.show()
QTimer.singleShot(0, m.close)
app.exec_()
