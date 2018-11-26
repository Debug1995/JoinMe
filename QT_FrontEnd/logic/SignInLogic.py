import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from QT_FrontEnd.maindialog import *
from QT_FrontEnd.mainwindow import *
from QT_FrontEnd.registerdialog import *


class SignInWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SignInWindow, self).__init__(parent)
        self.setupUi(self)
        self.SignUpButton.clicked.connect(self.sign_up_button_clicked)
        self.QuitButton.clicked.connect(self.quit_button_clicked)

    def sign_up_button_clicked(self):
        sign_up_window.show()
        self.close()

    def quit_button_clicked(self):
        self.close()


class SignUpWindow(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(SignUpWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_in_window = SignInWindow()
    sign_up_window = SignUpWindow()
    sign_in_window.show()
    sys.exit(app.exec_())
