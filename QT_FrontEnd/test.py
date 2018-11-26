import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maindialog import *


class MyWindow(QMainWindow, Ui_MainDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
